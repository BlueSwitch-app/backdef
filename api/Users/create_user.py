from ..index import userscollection, app
from flask import request, jsonify
from ...models.CreateUserObject import User
@app.route("/create_user", methods=["POST"])
def create_user():
    data = request.json
    try:
        user = User(
            nombre=data["nombre"],
            email=data["email"],
            password=data["password"],
            city=data["city"],
            phone=data["phone"]
        )
        userscollection.insert_one(user.__dict__)
        return jsonify({"mensaje": "Usuario creado con exito"})
    except Exception as e:
        return jsonify({"error": str(e)})