import logging
import json
from app.agents.config_ai import get_ai_response

def executer_tache_analyse():
    logging.info("--- [Analyste] : Calcul des performances ---")
    # Simulation de lecture de données (à connecter à ton historique de ventes)
    donnees = "Chiffre d'affaires aujourd'hui : 150 euros. Taux de conversion : 2.5%."
    prompt = f"Analyse ces performances : {donnees}. Propose deux axes d'amélioration pour demain."
    strategie = get_ai_response(prompt)
    
    with open("app/missions/rapport_financier.txt", "w") as f:
        f.write(strategie)
    logging.info("--- [Analyste] : Rapport généré ---")
