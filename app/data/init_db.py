import sqlite3

def init_db():
    conn = sqlite3.connect('app/data/ventes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS commandes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_email TEXT,
            service_vendu TEXT,
            montant REAL,
            statut TEXT,
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("Base de données initialisée.")

if __name__ == "__main__":
    init_db()
