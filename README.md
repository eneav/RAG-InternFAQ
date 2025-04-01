
#  RAG-Intern-FAQ (LangChain + OpenAI + FAISS)

Dieses Projekt demonstriert ein Retrieval-Augmented Generation (RAG) System auf Basis von LangChain, OpenAI und FAISS. Es beantwortet Fragen auf Grundlage einer lokal vektorisierten Wissensdatenbank (basierend auf CSV-Inhalten).

## Features
- Embedding-basierte Ähnlichkeitssuche (FAISS)
- GPT-Modell (z. B. GPT-3.5 oder GPT-4) über `.env` steuerbar
- Lokale Verarbeitung, kein Chroma oder Cloud-Zwang
- Unterstützung für `.env` und `.env.example` zur sicheren Konfiguration

## Setup

1. Virtuelle Umgebung aktivieren (falls noch nicht vorhanden erstellen):
```bash
python -m venv .venv
.\.venv\Scriptsctivate
```

2. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

3. `.env` anlegen (basierend auf `.env.example`) und OpenAI API Key + Modell definieren:
```env
OPENAI_API_KEY=your-key-here
GPT_MODEL=gpt-3.5-turbo
```

##  Nutzung

### Datenbank aus CSV-Datei erzeugen:
```bash
python create_database.py
```

### Eine Frage stellen:
```bash
python main.py
```

> Alternativ kann man `query_data.py` direkt ausführen und eine Frage über die Kommandozeile mitgeben.

## Projektstruktur

- `create_database.py` – Erstellt die FAISS-Datenbank aus CSV
- `query_data.py` – Führt eine vektorbasierte Suche durch und holt GPT-Antworten
- `main.py` – Einstiegspunkt zum Testen
- `data/` – Enthält CSV-Dateien (nicht im Repo enthalten)
- `faiss_index/` – Persistente Vektordatenbank (nicht im Repo enthalten)
- `.env.example` – Vorlage für Konfigurationswerte 

##  Technologien

- [LangChain](https://www.langchain.com/)
- [OpenAI GPT](https://platform.openai.com/)
- [FAISS (Meta)](https://github.com/facebookresearch/faiss)
- [Python](https://www.python.org/)


## Eigene CSV hochladen

Um eigene Daten zu verwenden, lege eine CSV-Datei im Ordner `data/` ab. Diese sollte die folgenden zwei Spalten enthalten:

| Fragen                        | Antworten                                                |
|------------------------------|-----------------------------------------------------------|
| Wie melde ich mich krank?    | Krankmeldungen bis 9 Uhr per Telefon oder E-Mail melden. |
| Wie viel Urlaub habe ich?    | 30 Urlaubstage im Jahr laut Vertrag.                     |

> Hinweis: Diese Datei wird **nicht im Repository gespeichert**. Sie ist in `.gitignore` ausgeschlossen.

>>>>>>> 38213f0 (Removed sensitive CSV and added to .gitignore)
