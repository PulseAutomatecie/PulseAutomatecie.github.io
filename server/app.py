import os
from flask import Flask, jsonify, request
import stripe
from dotenv import load_dotenv
from flask_cors import CORS

# Charger les clés depuis le fichier .env à la racine
load_dotenv(dotenv_path='../.env')

app = Flask(__name__)
CORS(app)
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'eur',
                    'unit_amount': 2000, # Prix en centimes (ici 20.00 €)
                    'product_data': {
                        'name': 'Service Automatisé Premium',
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://pulseautomatecie.github.io/success.html',
            cancel_url='https://pulseautomatecie.github.io/cancel.html',
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run(port=5001)
