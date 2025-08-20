
from ..index import app, teamscollection
from flask import request,jsonify


@app.route("/api/Teams/get_members", methods=['POST'])
def get_members():
    data = request.json
    team_code = data['team_code']
    if not team_code:
        return jsonify({"mensaje": "El código del equipo es requerido"}), 400
    team = teamscollection.find_one({'StringId': team_code})
    if not team:
        return jsonify({"mensaje": "El equipo no existe"}), 404
    return jsonify({"members": team.get('Members', [])}), 200
