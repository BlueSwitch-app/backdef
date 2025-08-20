from ..index import app, userscollection
from flask import request,jsonify

@app.route("/update_user", methods=["POST"])
def update_user():
    data = request.get_json()
    email = data.get("email")
    if not email:
        return jsonify({"success": False, "error": "Email is required"}), 400

    update_fields = {k: v for k, v in data.items() if v and k != "email"}
    result = userscollection.update_one({"email": email}, {"$set": update_fields})

    if result.matched_count > 0:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": "User not found"}), 404
