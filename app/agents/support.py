import logging
from app.agents.config_ai import get_ai_response

def executer_tache_support(message_client):
    logging.info("--- [Support] : Analyse du message client ---")
    prompt = f"Tu es le responsable support client de PulseAutomate. Analyse ce message et rédige une réponse professionnelle et efficace : {message_client}"
    reponse = get_ai_response(prompt)
    with open("app/missions/reponse_support.txt", "w") as f:
        f.write(reponse)
    logging.info("--- [Support] : Réponse générée ---")
    return reponse
