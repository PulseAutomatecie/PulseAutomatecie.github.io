import logging
import os
from app.agents.config_ai import get_ai_response

def executer_tache_pdg():
    logging.info("--- [PDG] : Analyse des données et déploiement de stratégie ---")
    
    # Chemin vers le rapport financier
    rapport_path = "app/missions/rapport_financier.txt"
    rapport_contenu = "Aucun rapport disponible pour le moment."
    
    # Lecture du rapport si disponible
    if os.path.exists(rapport_path):
        with open(rapport_path, "r") as f:
            rapport_contenu = f.read()
            logging.info("--- [PDG] : Rapport financier chargé avec succès ---")
    
    # Prompt stratégique avec boucle de rétroaction
    prompt = f"""
    Tu es le PDG de PulseAutomate. 
    Rapport financier reçu : 
    {rapport_contenu}
    
    Ta mission :
    1. Analyse les faiblesses identifiées dans le rapport.
    2. Définis une stratégie prioritaire pour les prochaines 24h.
    3. Donne des instructions précises au Codeur pour améliorer les points faibles (taux de conversion, design, contenu).
    """
    
    # Appel à l'IA avec gestion de la cascade (Gemini/Groq/Mistral/DeepSeek/Ollama)
    strategie = get_ai_response(prompt)
    
    # Enregistrement de la stratégie
    with open("app/missions/strategie_actuelle.txt", "w") as f:
        f.write(strategie)
    
    logging.info("--- [PDG] : Stratégie enregistrée dans app/missions/strategie_actuelle.txt ---")

if __name__ == "__main__":
    executer_tache_pdg()
