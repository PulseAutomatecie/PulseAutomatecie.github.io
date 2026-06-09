import logging
import os
import subprocess

def executer_tache_déployeur():
    logging.info("--- [Déployeur] : Lancement du push vers GitHub ---")
    
    # Ton dossier est celui où tu te trouves actuellement
    dossier_repo = "/root/production/drop-servicing-1"

    try:
        os.chdir(dossier_repo)
        
        # 1. Ajouter le fichier index.html qui a été généré
        subprocess.run(["git", "add", "index.html"], check=True)
        
        # 2. Commit avec un message clair
        subprocess.run(["git", "commit", "-m", "Usine : Mise à jour automatique du design"], check=True)
        
        # 3. Pousser vers GitHub
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        logging.info("--- [Déployeur] : Push vers GitHub réussi ---")
        return True
        
    except subprocess.CalledProcessError as e:
        logging.error(f"--- [Déployeur] : Erreur Git : {e} ---")
        return False
    except Exception as e:
        logging.error(f"--- [Déployeur] : Erreur critique : {e} ---")
        return False
