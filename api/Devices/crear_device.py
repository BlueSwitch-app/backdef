from ..index import app, devicescollection
from ..models.NewDevicesObject import Producto
from flask import request,jsonify
from datetime import datetime
import uuid
@app.route("/api/Devices/crear_device", methods=["POST"])
def crear_producto():
    data = request.get_json()
    if not data:
        return jsonify({"mensaje": "No se recibió información"}), 400

    campos_requeridos = ["nombre", "categoria", "watts", "color", "team_code", "email"]
    for campo in campos_requeridos:
        if campo not in data or data[campo] == "" or data[campo] is None:
            return jsonify({"mensaje": f"All fields are required"}), 400

    try:
        producto = Producto(
            nombre=data["nombre"],
            categoria=data["categoria"],
            watts=data["watts"],
            color=data["color"],
            state=True,
            email=data["email"],
            created_at=[],
            team=data["team_code"]
        )
        producto_dict = producto.model_dump(exclude_unset=False)
        producto_dict["stringid"] = str(uuid.uuid4())
        producto_dict["created_at"] = [[datetime.now().isoformat(), None]]
        devicescollection.insert_one(producto_dict)
        return jsonify({"mensaje": "Producto creado exitosamente"}), 200
    except Exception as e:
        return jsonify({"mensaje": "Error inesperado en el servidor", "error": str(e)}), 500
