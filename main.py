from create_database import generate_data_store
from query_data import run_query

def main():
    print("\n DATENBANK WIRD NEU AUFGEBAUT...")
    generate_data_store()

    print("\n Starte Abfragebeispiel:")
    query = input("Frage eingeben: ")
    run_query(query)

if __name__ == "__main__":
    main()
