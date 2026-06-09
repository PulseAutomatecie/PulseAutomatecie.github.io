import sqlite3
from datetime import datetime

def executer_tache_comptable():
    conn = sqlite3.connect('app/data/ventes.db')
    cursor = conn.cursor()

    # Récupérer toutes les ventes validées
    cursor.execute("SELECT montant FROM commandes WHERE statut = 'Payé'")
    ventes = cursor.fetchall()

    total_ca = sum(row[0] for row in ventes)
    nombre_ventes = len(ventes)

    # Création du rapport de statistiques
    rapport = f"""
    --- Rapport Comptable PulseAutomate ---
    Date du rapport : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    Nombre total de ventes : {nombre_ventes}
    Chiffre d'Affaires total : {total_ca:.2f} €
    ---------------------------------------
    """

    with open("app/missions/statistiques.txt", "w") as f:
        f.write(rapport)

    conn.close()
    print("Agent Comptable : Rapport de statistiques mis à jour.")

if __name__ == "__main__":
    executer_tache_comptable()











