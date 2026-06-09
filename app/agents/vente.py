import logging
import os
from app.agents.config_ai import get_ai_response

def executer_tache_vente():
    logging.info("--- [Vente] : Début du travail de copywriting AIDA ---")
    
    try:
        # 1. Lecture sécurisée de la stratégie marketing
        strategie = "Stratégie non disponible."
        if os.path.exists("app/missions/marketing_result.txt"):
            with open("app/missions/marketing_result.txt", "r", encoding="utf-8") as f:
                strategie = f.read()
        else:
            logging.warning("--- [Vente] : Fichier marketing_result.txt non trouvé, utilisation d'un défaut ---")

        # 2. Génération du contenu AIDA via l'IA
        prompt = f"""Tu es un copywriter expert en conversion. Analyse cette stratégie : {strategie}.
        Rédige le contenu du site en utilisant strictement la structure AIDA :
        1. ATTENTION : Accroche percutante ciblant une douleur précise.
        2. INTÉRÊT : Liste 3 bénéfices clés (gain de temps/argent).
        3. DÉSIR : Témoignage client fictif et élément d'urgence.
        4. ACTION : Appel à l'action très incitatif.
        Ton : Professionnel, persuasif, orienté résultat."""

        resultat = get_ai_response(prompt)

        # 3. Écriture du contenu pour l'agent Codeur
        with open("app/missions/vente_result.txt", "w", encoding="utf-8") as f:
            f.write(resultat)

        logging.info("--- [Vente] : Leviers de vente AIDA optimisés et enregistrés ---")

    except Exception as e:
        logging.error(f"--- [Vente] : Erreur critique durant la génération du contenu de vente : {e} ---")
