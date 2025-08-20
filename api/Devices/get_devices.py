from ..index import app, devicescollection
from flask import request,jsonify



@app.route("/get_devices", methods=["POST"])
def get_devices():
    data = request.get_json()
    email = data.get("email")
    team_code = data.get("team_code")
    if not email and not team_code:
        return jsonify({"error": "Either email or team_code is required"}), 400

    query = {"email": email} if email else {"team": team_code}
    devices = list(devicescollection.find(query, {"_id": False}))
    return jsonify(devices), 200