import sys
import os
import subprocess
import time
import logging

# Configuration pour permettre les imports depuis la racine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents import (analyste, designer, comptable, marketing, 
                    vente, com, codeur, architecte, telegram_bot)

# Configuration des logs
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()])

# Groupes d'agents
CYCLE_1 = [analyste.executer_tache_analyste, marketing.executer_tache_marketing]
CYCLE_2 = [designer.executer_tache_designer, vente.executer_tache_vente]
CYCLE_3 = [com.executer_tache_com, comptable.executer_tache_comptable, 
           architecte.executer_tache_architecte, telegram_bot.executer_tache_bot]
CYCLE_FINAL = [codeur.executer_tache_codeur]

def verifier_conformite_legale():
    """Vérifie la sécurité des contenus avant déploiement."""
    mots_interdits = ["fraude", "arnaque", "spam", "promesse irréaliste"]
    try:
        if os.path.exists("index.html"):
            with open("index.html", "r") as f:
                contenu = f.read().lower()
                for mot in mots_interdits:
                    if mot in contenu:
                        logging.error(f"--- [ALERTE LÉGALE] : Contenu suspect détecté : {mot} ---")
                        return False
        return True
    except Exception as e:
        logging.error(f"--- [PDG] : Erreur lors de l'audit légal : {e} ---")
        return False

def pdg_orchestrateur():
    logging.info("--- [PDG] : Démarrage du système PulseAutomate - Objectif : Profit Légal ---")
    telegram_bot.executer_tache_bot("<b>Système PulseAutomate :</b> Démarrage et test de connexion OK.")
    
    while True:
        try:
            # Exécution des cycles
            for i, groupe in enumerate([CYCLE_1, CYCLE_2, CYCLE_3, CYCLE_FINAL], 1):
                logging.info(f"--- [PDG] : Démarrage du cycle de travail {i}/4 ---")
                for agent_task in groupe:
                    try:
                        agent_task()
                        time.sleep(15) 
                    except Exception as e:
                        logging.error(f"Erreur agent dans cycle {i} : {e}")
                time.sleep(60) 
            
            # Audit et Déploiement
            if verifier_conformite_legale():
                logging.info("--- [PDG] : Audit légal validé. Déploiement en cours ---")
                subprocess.run(["git", "add", "."], check=True)
                subprocess.run(["git", "commit", "-m", "Auto-update conforme et rentable"], check=True)
                subprocess.run(["git", "push", "origin", "main"], check=True)
                logging.info("--- [PDG] : Cycle complet terminé avec succès. Repos 60 min ---")
            else:
                logging.error("--- [PDG] : Déploiement annulé pour non-conformité ---")
                telegram_bot.executer_tache_bot("<b>ALERTE :</b> Déploiement annulé. Audit légal échoué.")
            
            time.sleep(3600) 

        except Exception as e:
            error_msg = f"<b>ALERTE SYSTÈME :</b> L'usine s'est arrêtée.\n<b>Erreur :</b> {str(e)}"
            logging.error(f"--- [PDG] : ARRÊT CRITIQUE : {e} ---")
            telegram_bot.executer_tache_bot(message=error_msg)
            time.sleep(600)

if __name__ == "__main__":
    pdg_orchestrateur()
