from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# Erlaube Anfragen vom Frontend (läuft auf anderem Port/Container)
CORS(app)

@app.route('/')
def index():
    return jsonify({"message": "Backend is running!"})

# Platzhalter für den späteren Korrektur-Endpunkt
@app.route('/correct', methods=['POST'])
def correct_text_endpoint():
    # Später: Logik zum Extrahieren und Verarbeiten des Textes
    data = request.get_json()
    text = data.get('text', '')
    # Platzhalter: Gibt den Text einfach zurück
    corrected_text = text.upper() # Nur zum Testen
    return jsonify({"corrected_text": corrected_text})

# Kein 'if __name__ == "__main__":' Block nötig, wenn über Flask CLI oder Gunicorn gestartet wird
