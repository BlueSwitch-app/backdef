
from ..index import app, teamscollection,devicescollection,discardDevicesCollection
from flask import Blueprint, request,jsonify
teams_bp = Blueprint("teams", __name__)
@teams_bp.route("/api/Teams/leave_team", methods=['POST'])
def leave_team():
    data = request.json
    user_email = data['email']
    team_code = data['teamcode']
    teamscollection.update_one({'StringId': team_code}, {'$pull': {'Members':{'email': user_email}}})
    result = list(devicescollection.find({"email": user_email, "team": team_code}))
    for doc in result:
        doc.pop("_id", None)
    discardDevicesCollection.insert_many(result)
    devicescollection.update_many({"email": user_email, "team": team_code}, {"$set": {"team": "no_team"}})
    return jsonify({"mensaje": "El usuario ha dejado el equipo"}), 200
