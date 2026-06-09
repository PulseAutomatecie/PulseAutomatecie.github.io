import logging
import sys
import os

# Configuration du chemin pour les imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.agents.pdg import executer_tache_pdg
from app.agents.codeur import executer_tache_codeur
from app.agents.testeur import executer_tache_testeur
from app.agents.deployeur import executer_tache_déployeur
from app.agents.analyseur_revenus import executer_tache_analyse
from app.agents.support import executer_tache_support
from app.agents.telegram_bot import executer_tache_bot  # Import du bot Telegram

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def cycle_usine():
    logging.info("--- DÉMARRAGE DU CYCLE USINE COMPLET ---")
    try:
        # 1. Stratégie
        executer_tache_pdg()

        # 2. Qualité et Déploiement avec boucle de correction
        validation_reussie = False
        for tentative in range(2):
            logging.info(f"--- [Pulse] : Tentative de génération/correction {tentative + 1}/2 ---")
            executer_tache_codeur()
            if executer_tache_testeur():
                logging.info("--- [Pulse] : Code validé, lancement du déploiement ---")
                executer_tache_déployeur()
                validation_reussie = True
                break
            else:
                logging.warning(f"--- [Pulse] : Échec validation tentative {tentative + 1} ---")

        # 3. Finalisation et Analyse
        if validation_reussie:
            executer_tache_analyse()
            executer_tache_support("Analyse cycle terminée")
            # Notification de succès sur Telegram
            executer_tache_bot("🚀 <b>Usine :</b> Cycle complet, site déployé avec succès.")
        else:
            msg_erreur = "❌ <b>Erreur Usine :</b> Échec de validation après 2 tentatives."
            logging.error(msg_erreur)
            executer_tache_bot(msg_erreur)

        logging.info("--- CYCLE TERMINÉ ---")

    except Exception as e:
        error_msg = f"⚠️ <b>Erreur Critique Usine :</b> {str(e)}"
        logging.error(f"--- ERREUR CRITIQUE DANS LE CYCLE : {e} ---")
        # Envoi de l'erreur critique sur Telegram
        executer_tache_bot(error_msg)

if __name__ == "__main__":
    cycle_usine()
