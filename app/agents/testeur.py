import logging
import os
from app.agents.config_ai import get_ai_response

def executer_tache_testeur():
    logging.info("--- [Testeur] : Validation du code généré ---")
    
    chemin_code = "app/missions/code_genere.txt"
    
    # Vérification de l'existence du fichier
    if not os.path.exists(chemin_code):
        logging.error("--- [Testeur] : Aucun fichier code_genere.txt trouvé ---")
        return False

    # Lecture sécurisée : on limite à 1000 caractères pour éviter l'erreur de taille de l'API
    with open(chemin_code, "r", encoding="utf-8") as f:
        code_partiel = f.read(1000)

    if not code_partiel.strip():
        logging.error("--- [Testeur] : Le fichier est vide ---")
        return False

    # Prompt allégé pour la validation
    prompt = f"Tu es un expert QA. Analyse ce début de code HTML/JS. Réponds uniquement par 'VALIDE' ou 'ERREUR' suivi d'une courte explication : \n{code_partiel}"

    resultat = get_ai_response(prompt)
    
    if resultat and "VALIDE" in resultat:
        logging.info(f"--- [Testeur] : Validation réussie : {resultat} ---")
        return True
    else:
        logging.error(f"--- [Testeur] : Échec validation : {resultat} ---")
        return False
