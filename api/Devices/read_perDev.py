from ..index import app
from flask import request,jsonify
from ..models.CO2AnalyticsperDev import CalculateCO2forDevice

@app.route("/api/Devices/read_perDev", methods=['POST'])
def read_perDev():
    data = request.json
    devices = data.get("data", [])
    try:
        CO2 = CalculateCO2forDevice(devices)
        return jsonify(CO2), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500