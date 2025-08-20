
from ..index import app, devicescollection, discardDevicesCollection
from flask import request,jsonify
from datetime import datetime

@app.route("/api/Devices/update_status", methods=['PUT'])
def update_device_status():
    data = request.get_json()
    device_id = data.get('id')
    new_status = data.get('status')
    args = data.get('argument')
    if device_id is None or new_status is None:
        return jsonify({'error': 'Faltan id o status'}), 400
    try:
        device = devicescollection.find_one({'stringid': device_id})
        if not device:
            return jsonify({'error': 'Dispositivo no encontrado'}), 404

        if args == "Switch":
            historial = device.get('created_at', [])
            now = datetime.utcnow().isoformat()
            if device.get('state') == new_status:
                return jsonify({'mensaje': 'El estado ya está actualizado'}), 200
            if new_status is True:
                historial.append([now, None])
            elif new_status is False and historial and historial[-1][1] is None:
                historial[-1][1] = now
            devicescollection.update_one({'stringid': device_id}, {'$set': {'state': new_status, 'created_at': historial}})
            return jsonify({'mensaje': 'Estado y fechas actualizados correctamente'}), 200
        elif args == "Delete":
            discardDevicesCollection.insert_one(device)
            devicescollection.delete_one({'stringid': device_id})
            return jsonify({'mensaje': 'Dispositivo eliminado correctamente'}), 200
        elif args == "Favorite":
            current_status = device.get('favorite', False)
            new_status = not current_status
            devicescollection.update_one({'stringid': device_id}, {'$set': {'favorite': new_status}})
            return jsonify({'mensaje': 'Estado actualizado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'No se ejecutó porque el argumento no es valido'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
