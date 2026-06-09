import os
import logging
from app.agents.config_ai import get_ai_response

def executer_tache_designer():
    logging.info("--- [Designer] : Début de la conception de la charte graphique ---")
    
    try:
        prompt = """Tu es le Designer UI/UX expert en psychologie de la vente pour PulseAutomate.
        Définis une charte graphique pour un service de drop-servicing B2B professionnel :
        - Palette : Bleu marine (confiance), Blanc (clarté), Or/Orange (action).
        - Typographie : Sans-serif moderne (Inter, Montserrat).
        - Hiérarchie : Boutons d'appel à l'action (CTA) à haut contraste.
        - Ambiance : Épurée, rassurante, haut de gamme, orientée conversion.
        
        Fournis les instructions sous forme de classes Tailwind CSS spécifiques pour chaque élément clé du site."""

        resultat = get_ai_response(prompt)

        # Enregistrement sécurisé de la charte pour le codeur
        with open("app/missions/design_result.txt", "w", encoding="utf-8") as f:
            f.write(resultat)

        logging.info("--- [Designer] : Charte graphique optimisée et enregistrée ---")

    except Exception as e:
        logging.error(f"--- [Designer] : Erreur lors de la conception : {e} ---")
