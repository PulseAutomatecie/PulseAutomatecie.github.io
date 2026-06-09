import os
import logging
from app.agents.config_ai import get_ai_response

def executer_tache_analyste():
    logging.info("--- [Analyste] : Début du cycle d'analyse et d'audit ---")
    
    try:
        # 1. Vérification de la qualité du travail précédent (Audit)
        if os.path.exists("index.html"):
            with open("index.html", "r", encoding="utf-8") as f:
                code_genere = f.read()

            # Lecture de la mission précédente
            mission_precedente = "Aucune mission définie."
            if os.path.exists("app/missions/marketing.txt"):
                with open("app/missions/marketing.txt", "r", encoding="utf-8") as f:
                    mission_precedente = f.read()

            prompt_audit = f"""Tu es le superviseur qualité de PulseAutomate.
            Analyse le code généré : {code_genere[:2000]}...
            Vérifie s'il respecte cette stratégie : {mission_precedente}.
            Évalue : 1. Psychologie de vente, 2. Clarté du message.
            Réponds par 'OK' si c'est parfait, sinon liste les points précis à améliorer pour le prochain cycle."""

            audit = get_ai_response(prompt_audit)
            logging.info("--- [Analyste] : Audit qualité terminé ---")

            # Enregistrement pour le codeur
            with open("app/missions/audit_result.txt", "w", encoding="utf-8") as f:
                f.write(audit)

        # 2. Définition de la nouvelle mission
        prompt_mission = """Analyse les dernières tendances du drop-servicing 
        et définis une mission marketing précise et innovante pour PulseAutomate pour le prochain cycle."""
        
        nouvelle_mission = get_ai_response(prompt_mission)

        with open("app/missions/marketing.txt", "w", encoding="utf-8") as f:
            f.write(nouvelle_mission)
            
        logging.info("--- [Analyste] : Nouvelle mission définie ---")

    except Exception as e:
        logging.error(f"--- [Analyste] : Erreur critique durant l'analyse : {e} ---")
