import os
import subprocess
from groq import Groq

# Configuration
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def piloter_entreprise():
    # 1. Analyse et Décision du PDG
    prompt = """
    Tu es le PDG autonome de PulseAutomate. 
    Ta mission : Choisir le service de drop-servicing le plus rentable aujourd'hui.
    Génère UNIQUEMENT le contenu HTML complet pour la page index.html.
    Ne mets aucune explication avant ou après le code HTML.
    Assure-toi que le design est professionnel et incite à l'action.
    """
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    contenu = response.choices[0].message.content
    
    # Nettoyage des balises markdown si l'IA en ajoute
    contenu = contenu.replace("```html", "").replace("```", "").strip()
    
    # 2. Application de la décision
    with open("index.html", "w") as f:
        f.write(contenu)
        
    # 3. Déploiement automatique
    subprocess.run(["git", "add", "index.html"], check=True)
    subprocess.run(["git", "commit", "-m", "PDG IA: Pivot stratégique auto-décidé"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    
    # 4. Enregistrement de la décision
    with open("journal_decisions.txt", "a") as f:
        f.write(f"Décision prise le 2026-06-08 : {contenu[:50]}...\n")

if __name__ == "__main__":
    piloter_entreprise()
