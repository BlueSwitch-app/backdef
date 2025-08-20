from ..index import app, teamscollection
from flask import request,jsonify
from ...models.CreateTeamObject import Team, TeamMember

@app.route('/api/Teams/create_team', methods=['POST'])
def create_team():
    data = request.json
    team_name = data['team_name']
    user_email = data['email']
    try:
        team = Team(Name=team_name, Members=[TeamMember(email=user_email, role="admin")])
        teamscollection.insert_one(team.model_dump())
        return jsonify({"mensaje": "Equipo creado con éxito", "team": team.dict()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
