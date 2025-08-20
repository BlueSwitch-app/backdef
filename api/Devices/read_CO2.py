from ..index import app, devicescollection
from flask import request, jsonify, Blueprint
from ..models.CO2Analytics import CalculateCO2
devices_bp = Blueprint("devices", __name__)
@devices_bp.route("/api/Devices/read-CO2", methods=["POST"])
def read_CO2():
    data = request.get_json()
    email = data.get("email")
    team_code = data.get("team_code")
    if not email and not team_code:
        return jsonify({"error": "Email or team_code required"}), 400
    devices = list(devicescollection.find({"email": email} if email else {"team": team_code}, {"_id": False}))
    total_CO2, max_device_info = CalculateCO2(devices)
    return jsonify({"total_CO2": total_CO2, "device_mas_CO2": max_device_info}), 200
