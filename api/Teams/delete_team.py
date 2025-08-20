
from ..index import app, teamscollection
from flask import request,jsonify


@app.route("/api/Teams/delete_team", methods=['POST'])
def delete_team():
    data = request.json
    team_code = data['teamcode']
    if not team_code:
        return jsonify({"mensaje": "El código del equipo es requerido"}), 400
    teamscollection.delete_one({'StringId': team_code})
    return jsonify({"mensaje": "El equipo ha sido eliminado"}), 200