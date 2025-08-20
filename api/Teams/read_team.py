
from ..index import app, teamscollection
from flask import Blueprint, request,jsonify
teams_bp = Blueprint("teams", __name__)
@teams_bp.route("/api/Teams/read_team", methods=['POST'])
def read_teams():
    data = request.json
    user_email = data['email']
    teams_cursor = teamscollection.find({'Members.email': user_email})
    teams = []
    for team in teams_cursor:
        for member in team.get('Members', []):
            if member.get('email') == user_email:
                teams.append({'name': team.get('Name'), 'code': team.get('StringId'), 'role': member.get('role')})
                break
    return jsonify({'teams': teams}), 200
