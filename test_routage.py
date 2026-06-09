import logging
from app.agents.config_ai import get_ai_response

# Configuration simple pour le test
logging.basicConfig(level=logging.INFO)

def verifier_routage():
    logging.info("--- DÉBUT DU TEST DE ROUTAGE DES MODÈLES ---")
    
    # On envoie une question simple pour tester la réponse
    prompt = "Réponds uniquement par : 'Le routage fonctionne'."
    
    try:
        reponse = get_ai_response(prompt)
        logging.info(f"Réponse reçue : {reponse}")
        logging.info("--- TEST RÉUSSI ---")
    except Exception as e:
        logging.error(f"Le routage a échoué : {e}")

if __name__ == "__main__":
    verifier_routage()
