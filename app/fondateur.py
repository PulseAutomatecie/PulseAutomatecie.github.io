import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def choisir_business():
    prompt = """
    Tu es un expert en entrepreneuriat numérique et drop-servicing. 
    Ta mission : Proposer une opportunité de business ultra-rentable et automatisable 
    que nous pouvons lancer immédiatement via PulseAutomate.
    Analyse les tendances actuelles.
    Donne :
    1. Le service exact à vendre.
    2. La cible client (qui va payer).
    3. Pourquoi c'est automatisable par une IA.
    4. Le prix de vente suggéré.
    """
    
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    print("--- Analyse de marché en cours pour gagner le pari ---")
    print(choisir_business())
