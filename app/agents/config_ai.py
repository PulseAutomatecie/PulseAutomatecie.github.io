import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

def get_ai_response(prompt):
    """
    Gestionnaire intelligent de requêtes IA avec failover en cascade.
    """
    fournisseurs = ["GOOGLE", "GROQ", "MISTRAL", "DEEPSEEK", "OLLAMA"]

    for nom in fournisseurs:
        logging.info(f"--- [AI] : Tentative de génération avec {nom} ---")
        try:
            if nom == "GOOGLE":
                import google.generativeai as genai
                genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
                
                # Modèle confirmé disponible dans tes logs
                model = genai.GenerativeModel("models/gemini-2.0-flash")
                response = model.generate_content(prompt)
                
                if response and response.text:
                    return response.text
                else:
                    raise Exception("Réponse vide reçue de Google")

            elif nom == "GROQ":
                headers = {"Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}"}
                payload = {"model": "llama-3.1-8b-instant", "messages": [{"role": "user", "content": prompt}]}
                res = requests.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers, timeout=30)
                if res.status_code == 200: 
                    return res.json()['choices'][0]['message']['content']

            elif nom == "MISTRAL":
                headers = {"Authorization": f"Bearer {os.getenv('MISTRAL_API_KEY')}"}
                payload = {"model": "mistral-small-latest", "messages": [{"role": "user", "content": prompt}]}
                res = requests.post("https://api.mistral.ai/v1/chat/completions", json=payload, headers=headers, timeout=30)
                if res.status_code == 200: 
                    return res.json()['choices'][0]['message']['content']

            elif nom == "DEEPSEEK":
                headers = {"Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}"}
                payload = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}
                res = requests.post("https://api.deepseek.com/chat/completions", json=payload, headers=headers, timeout=30)
                if res.status_code == 200: 
                    return res.json()['choices'][0]['message']['content']

            elif nom == "OLLAMA":
                res = requests.post(
                    "http://172.17.0.1:11434/api/generate",
                    json={"model": "llama3.2:1b", "prompt": prompt, "stream": False},
                    timeout=500
                )
                if res.status_code == 200:
                    return res.json().get("response", "")

        except Exception as e:
            logging.warning(f"--- [AI] : {nom} a échoué : {str(e)[:50]}... ---")
            continue

    return "ERREUR_CRITIQUE_TOUS_FOURNISSEURS_INDISPONIBLES"
