
from ..index import app, teamscollection
from flask import request,jsonify


@app.route("/api/Teams/update_members", methods=['POST'])
def update_members():
    data = request.json
    team_code = data['teamcode']
    user_email = data['email']
    mode = data['action']
    if not team_code or not user_email:
        return jsonify({"mensaje": "teamcode y email requeridos"}), 400
    if mode == "promote":
        teamscollection.update_one({'StringId': team_code, 'Members.email': user_email}, {'$set': {'Members.$.role': 'assistant'}})
        return jsonify({"mensaje": "El usuario ha sido promovido a asistente"}), 200
    elif mode == "demote":
        teamscollection.update_one({'StringId': team_code, 'Members.email': user_email}, {'$set': {'Members.$.role': 'member'}})
        return jsonify({"mensaje": "El usuario ha sido degradado a miembro"}), 200
    elif mode == "delete":
        teamscollection.update_one({'StringId': team_code}, {'$pull': {'Members': {'email': user_email}}})
        return jsonify({"mensaje": "El usuario ha sido eliminado del equipo"}), 200
    else:
        return jsonify({"mensaje": "La acción no es válida"}), 400
