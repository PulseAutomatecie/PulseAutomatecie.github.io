from app.agents.pdg import executer_tache_pdg
import logging

logging.basicConfig(level=logging.INFO)
print("--- Test du PDG ---")
try:
    executer_tache_pdg()
    print("--- Test réussi ! ---")
except Exception as e:
    print(f"--- Erreur : {e} ---")
