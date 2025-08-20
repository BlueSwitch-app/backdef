from ..index import app, teamscollection
from flask import Blueprint, request,jsonify


teams_bp = Blueprint("teams", __name__)
@teams_bp.route('/api/Teams/join_team', methods=['POST'])
def join_team():
    data = request.json
    team_name = data['team_name']
    user_email = data['email']
    team_code = data['team_code']
    team = teamscollection.find_one({'Name': team_name, 'StringId': team_code})
    if not team:
        return jsonify({"mensaje": "El equipo no existe o el código es incorrecto"}), 400
    for member in team.get('Members', []):
        if member.get('email') == user_email:
            return jsonify({"mensaje": "Ya eres miembro del equipo"}), 400
    teamscollection.update_one({'Name': team_name, 'StringId': team_code}, {'$push': {'Members': {'email': user_email, 'role': 'member'}}})
    return jsonify({"mensaje": "Te uniste al equipo con éxito"}), 200
