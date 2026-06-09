import os
# Supprime le droit d'écriture sur le fichier index.html pour bloquer le PDG
os.chmod("index.html", 0o444)
print("Système bloqué. Le PDG ne peut plus modifier le site.")
