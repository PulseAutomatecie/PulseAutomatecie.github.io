import os
import logging
from app.agents.config_ai import get_ai_response

def executer_tache_marketing():
    logging.info("--- [Marketing] : Début de la stratégie marketing ---")
    
    try:
        # 1. Lecture de la mission définie par l'analyste
        besoin = "Mission marketing non définie."
        if os.path.exists("app/missions/marketing.txt"):
            with open("app/missions/marketing.txt", "r", encoding="utf-8") as f:
                besoin = f.read()

        # 2. Génération de la stratégie par l'IA
        prompt = f"""Tu es l'expert marketing de PulseAutomate. 
        Analyse cette mission : {besoin}. 
        Définis précisément la cible client B2B et l'argument de vente principal (Unique Selling Proposition) 
        pour maximiser le taux de conversion sur notre site."""
        
        resultat = get_ai_response(prompt)

        # 3. Écriture du résultat pour l'Agent Vente et l'Agent Codeur
        with open("app/missions/marketing_result.txt", "w", encoding="utf-8") as f:
            f.write(resultat)

        logging.info("--- [Marketing] : Stratégie marketing générée et enregistrée ---")

    except Exception as e:
        logging.error(f"--- [Marketing] : Erreur critique lors de la stratégie : {e} ---")
