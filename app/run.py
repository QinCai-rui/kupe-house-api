from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

facts = [
    "In Māori tradition, Kupe is celebrated as a prominent early explorer of New Zealand.",
    "Kupe named New Zealand 'Aotearoa', meaning 'land of the long white cloud'.",
    "Kupe returned to his homeland after discovering New Zealand, promising to return, but unfortunately did not.",
    "According to legends, Kupe battled Te Wheke-a-Muturangi (giant octopus).",
    "Kupe's journey is often linked with the Hokianga Harbour, considered one of his landing points in New Zealand.",
    "The exact timeline of Kupe's voyage is unknown, and is debated among historians and Māori scholars.",
    "In some Māori traditions, Kupe is associated with the introduction of certain native species to New Zealand.",
    "Kupe's navigational skills allowed him to cross vast stretches of the Pacific Ocean using stars, currents, winds, wave echoes, and land shadows.",
    "Kupe House's mascot is the kiwi, a flightless bird native to New Zealand.",
    "Kupe House participates in annual inter-house cultural performances.",
    "Kupe House has won multiple competitions, including house sports, at Macleans College.",
    "The values of Kupe House include kindness, understanding, perseverance, and enthusiasm (KUPE).",
    "The legend of Kupe has inspired numerous artworks and other creations in New Zealand.",
    "Kupe’s journey enabled Polynesians to settle in New Zealand, as later Māori waka followed the path he navigated.",
    "Kupe is credited with naming key landmarks in New Zealand, such as The Hokianga Harbour.",
    "The suggested dates for Kupe’s arrival in New Zealand range from 925 CE to the mid-14th century."
]

@app.route('/api', methods=['GET'])
def random_fact():
    fact = random.choice(facts)
    return jsonify({'fact': fact})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
