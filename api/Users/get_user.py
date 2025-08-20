from ..index import app, userscollection
from flask import request, jsonify

@app.route("/get_user", methods=['POST'])
def get_user_info():
    data = request.json
    email = data.get('email')
    try:
        user = userscollection.find_one({"email": email}, {"_id": False})
        return jsonify(user), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500