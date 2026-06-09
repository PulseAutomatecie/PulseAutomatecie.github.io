import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.json
    # Logique simplifiée pour l'exemple
    conn = sqlite3.connect('app/data/ventes.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO commandes (client_email, service_vendu, montant, statut) VALUES (?, ?, ?, ?)",
                   (payload['email'], payload['service'], payload['montant'], 'Payé'))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(port=5000)
