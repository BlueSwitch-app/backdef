from ..index import app, userscollection
from flask import request,jsonify
from ...models.UploadCloudinary import upload_image
@app.route("/api/Users/upload_avatar", methods=["POST"])
def upload_avatar():
    data = request.get_json()
    email = data.get("email")
    imageUri = data.get("imageUri")
    if not email or not imageUri:
        return jsonify({"success": False, "error": "Email and avatar are required"}),400
    
    try:
        avatar = upload_image(imageUri)
        userscollection.update_one({"email": email}, {"$set": {"avatar": avatar}})
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500