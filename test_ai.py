from app.agents.config_ai import get_ai_response

print("--- Lancement du test de cascade IA ---")
resultat = get_ai_response("Donne-moi une phrase très courte de test pour vérifier que tu fonctionnes.")
print(f"--- Résultat reçu : {resultat} ---")
