from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

FAISS_PATH = "faiss_index"
PROMPT_TEMPLATE = """
Du beantwortest Nutzerfragen streng auf Basis des Kontexts.
Wenn du etwas nicht sicher weißt, sag: "Diese Information liegt mir nicht vor."

Kontext:
{context}

---

Frage: {question}
"""

def run_query(query_text):
    embedding_function = OpenAIEmbeddings()
    db = FAISS.load_local(FAISS_PATH, OpenAIEmbeddings(), allow_dangerous_deserialization=True)

    results = db.similarity_search_with_relevance_scores(query_text, k=3)

# der wert 0.3 ist ein schwellenwert (confidence level) für die ähnlichkeit
# je niedriger der wert, desto mehr (auch ungenaue) ergebnisse kommen durch
# je höher, desto strenger wird gefiltert
# kann angepasst werden, um das verhalten feinzujustieren


    if not results or results[0][1] < 0.3:                                          
        print("KEINE PASSENDEN ERGEBNISSE GEFUNDEN.")
        print("Bitte versuchen Sie es mit einer anderen Frage.")
        return

    context = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE).format(context=context, question=query_text)

    selected_model = os.getenv("GPT_MODEL", "gpt-3.5-turbo")
    model = ChatOpenAI(model=selected_model, temperature=0)
    response = model.predict(prompt)
    print(f"\n Antwort: {response}")