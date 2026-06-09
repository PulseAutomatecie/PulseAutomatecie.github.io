import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

def executer_tache_bot(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if not token or not chat_id:
        logging.error("--- [Telegram] : Erreur, clés manquantes dans .env ---")
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "HTML"}

    try:
        requests.post(url, data=payload, timeout=10).raise_for_status()
        logging.info("--- [Telegram] : Message envoyé à JB ---")
        return True
    except Exception as e:
        logging.error(f"--- [Telegram] : Échec envoi : {e} ---")
        return False
