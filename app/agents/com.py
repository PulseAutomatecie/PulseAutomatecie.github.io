import logging
import os
from app.agents.config_ai import get_ai_response

def executer_tache_com():
    logging.info("--- [Communication] : Début de la rédaction des emails de prospection ---")
    
    try:
        # 1. Lecture sécurisée de la stratégie
        strategie = "Stratégie non définie."
        if os.path.exists("app/missions/marketing_result.txt"):
            with open("app/missions/marketing_result.txt", "r", encoding="utf-8") as f:
                strategie = f.read()
        else:
            logging.warning("--- [Communication] : marketing_result.txt absent, utilisation du défaut ---")

        # 2. Génération des emails de prospection
        prompt = f"""Tu es un expert en prospection B2B. Basé sur cette stratégie : {strategie}, 
        rédige 3 emails de prospection hautement qualifiés :
        - Objet : Court (max 5 mots), orienté curiosité.
        - Contenu : Ton consultatif, focus sur les problèmes du prospect, sans jargon commercial.
        - Appel à l'action : 'Low-friction' (ex: 'Est-ce que ça vaut la peine d'en discuter 5 min ?').
        Sois ultra-personnalisé et professionnel."""

        resultat = get_ai_response(prompt)

        # 3. Sauvegarde pour les futures étapes (envoi auto, CRM, etc.)
        with open("app/missions/prospection_result.txt", "w", encoding="utf-8") as f:
            f.write(resultat)

        logging.info("--- [Communication] : Campagne de prospection prête ---")

    except Exception as e:
        logging.error(f"--- [Communication] : Erreur critique durant la génération des emails : {e} ---")
