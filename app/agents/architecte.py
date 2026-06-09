import logging
import os
from app.agents.config_ai import get_ai_response

def executer_tache_architecte():
    logging.info("--- [Architecte] : Vérification des besoins d'expansion ---")
    
    # Le PDG dépose ses besoins dans un fichier 'besoins.txt'
    besoin_path = "app/missions/besoins.txt"
    
    if os.path.exists(besoin_path):
        with open(besoin_path, "r", encoding="utf-8") as f:
            besoin = f.read().strip()
            
        if besoin:
            logging.info(f"--- [Architecte] : Besoin détecté : {besoin} ---")
            
            # 1. Génération du code du nouvel agent
            prompt = f"""Tu es un ingénieur logiciel expert. Écris un agent Python pour l'usine PulseAutomate.
            Mission : {besoin}.
            Règles :
            - La fonction principale doit s'appeler 'executer_tache_[nom_agent]'.
            - Utilise les imports standards (os, logging).
            - Inclus une gestion d'erreur try/except complète.
            - N'inclus que le code source pur, sans markdown."""
            
            code_agent = get_ai_response(prompt).replace("```python", "").replace("```", "").strip()
            
            # 2. Détermination du nom de l'agent
            nom = besoin.split()[0].lower()
            fichier_path = f"app/agents/{nom}.py"
            
            # 3. Création du fichier
            with open(fichier_path, "w", encoding="utf-8") as f:
                f.write(code_agent)
            
            logging.info(f"--- [Architecte] : Nouvel agent {nom}.py déployé avec succès ---")
            
            # 4. Nettoyage du besoin
            os.remove(besoin_path)
    else:
        logging.info("--- [Architecte] : Aucun nouveau besoin détecté ---")
