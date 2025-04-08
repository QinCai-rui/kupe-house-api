from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

facts = [
    "In Māori tradition, Kupe is celebrated as the first explorer to reach New Zealand.",
    "Kupe named New Zealand 'Aotearoa' meaning 'land of the long white cloud'.",
    "Kupe House's mascot is the kiwi, a flightless bird native to New Zealand.",
    "Kupe House has won multiple competitions, including house sports, at Macleans College.",
    "The values of Kupe House include kindness, understanding, perseverance, and enthusiasm.",
    "Kupe returned to his homeland after discovering New Zealand, promising to return but unfortunately did not.",
    "Kupe's navigational skills allowed him to cross vast stretches of the Pacific Ocean."
]

@app.route('/api', methods=['GET'])
def random_fact():
    fact = random.choice(facts)
    return jsonify({'fact': fact})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
