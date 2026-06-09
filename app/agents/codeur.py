import logging
import os
from app.agents.config_ai import get_ai_response

def executer_tache_codeur():
    logging.info("--- [Codeur] : Injection de contenu haut de gamme ---")

    contexte = ""
    for f_name in ["design_result.txt", "vente_result.txt"]:
        path = f"app/missions/{f_name}"
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                contexte += f"\n--- {f_name} ---\n" + f.read()

    # Prompt spécialisé
    prompt = f"""Tu es un Lead UI Designer. Ta mission est de générer du HTML/Tailwind pour intégrer dans une page web.

    RÈGLES STRICTES :
    - N'utilise PAS les classes 'prose'.
    - Utilise une typographie moderne : text-white pour les titres, text-slate-400 pour les paragraphes.
    - Utilise des structures de grilles ou flexbox.
    - Ajoute des boutons CTA avec la classe 'bg-blue-600 hover:bg-blue-700 transition'.
    - Style global : Très propre, professionnel, aéré.
    - NE GÉNÈRE PAS DE BALISES HTML OU HEAD/BODY, juste le contenu HTML à insérer.

    CONTENU À INTÉGRER : {contexte}
    """

    contenu_genere = get_ai_response(prompt)
    contenu_genere = contenu_genere.replace("```html", "").replace("```", "").strip()

    try:
        template_path = "app/templates/base.html"
        with open(template_path, "r", encoding="utf-8") as f:
            template = f.read()

        # ICI : Le marqueur doit être identique à celui dans base.html
        marqueur = ""

        if marqueur in template:
            final_html = template.replace(marqueur, contenu_genere)
        else:
            # Fallback de sécurité
            final_html = template.replace("</body>", f"{contenu_genere}\n</body>")

        # Écriture propre
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(final_html)
        
        with open("app/missions/code_genere.txt", "w", encoding="utf-8") as f:
            f.write(final_html)

        logging.info("--- [Codeur] : Design généré et injecté avec succès ---")
    except Exception as e:
        logging.error(f"--- [Codeur] : Erreur critique : {e} ---")
        raise e
