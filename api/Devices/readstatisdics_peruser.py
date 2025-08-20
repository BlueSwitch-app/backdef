from ..index import app, devicescollection
from flask import request,jsonify
from ...models.CO2AnalyticsperDev import CalculateCO2forDevice
from ...models.WattsAnalytics import calculateWatts
import math 
@app.route("/api/Devices/readstatisdics_peruser", methods=["POST"])
def statistics_per_user():
    data = request.get_json()
    email = data.get("email")
    team_code = data.get("team_code")
    if not email or not team_code:
        return jsonify({"success": False, "error": "Email and team_code are required"}),400
    statistics = list(devicescollection.find({"email": email, "team": team_code}, {"_id": False}))
    if not statistics:
        return jsonify({"success": True, "data": {"CO2": 0, "numdevices": 0, "trees": 0, "watts": 0}}), 200
    CO2 = CalculateCO2forDevice(statistics)
    Watts = calculateWatts(statistics)
    co2_value = CO2[0][0] if CO2 and CO2[0][0] else 0
    trees_value = math.ceil(co2_value / 22)
    return jsonify({"success": True, "data": {"CO2": co2_value, "numdevices": len(statistics), "trees": trees_value, "watts": Watts if Watts else 0}}), 200
