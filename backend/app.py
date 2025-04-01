from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from corrections.casual_rules import apply_corrections # Importiere die Korrekturfunktion aus dem neuen Modul

app = Flask(__name__)
# Erlaube Anfragen vom Frontend (läuft auf anderem Port/Container)
# Passe ggf. die origins an, wenn dein Frontend auf einer anderen URL läuft
CORS(app, resources={r"/correct": {"origins": "*"}}) # Erlaube alle Origins für /correct

@app.route('/')
def index():
    return jsonify({"message": "Backend is running!"})

@app.route('/correct', methods=['POST'])
def correct_text_endpoint():
    """
    Nimmt Text via POST entgegen, wendet Korrekturen an und gibt das Ergebnis zurück.
    """
    if not request.is_json:
        abort(400, description="Request must be JSON")

    data = request.get_json()
    text_to_correct = data.get('text') # Kein Default-Wert, um None zu erkennen

    if text_to_correct is None:
        # Wenn 'text' fehlt oder null ist
        abort(400, description="Missing 'text' field in JSON payload")
    elif not isinstance(text_to_correct, str):
        # Wenn 'text' kein String ist
        abort(400, description="'text' field must be a string")
    elif not text_to_correct:
         # Wenn 'text' ein leerer String ist, direkt zurückgeben
         return jsonify({"corrected_text": ""})

    # Wende die Korrekturen an
    corrected_text = apply_corrections(text_to_correct)

    return jsonify({"corrected_text": corrected_text})

# Kein 'if __name__ == "__main__":' Block nötig, wenn über Flask CLI oder Gunicorn gestartet wird
# Der Server wird über 'flask run' oder einen WSGI-Server wie Gunicorn gestartet.
