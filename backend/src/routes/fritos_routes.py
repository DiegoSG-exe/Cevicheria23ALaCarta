from flask import Blueprint, request, jsonify
from src.models import db
from src.models.models import Frito

fritos = Blueprint('fritos', __name__)

@fritos.route('/fritos', methods=['GET'])
def listFritos():
    try:
        fritos = Frito.query.all()
        fritos_json = []
        for frito in fritos:
            fritos_json.append({
                "id": frito.id,
                "nombre": frito.name,
                "precio": frito.precio
            })
        if fritos_json != []:
            return jsonify(fritos_json)
        else:
            return jsonify({"mensaje": "no hay fritos"})
    except Exception as e:
        return jsonify({"mensaje": "error al buscar fritos"})
    
@fritos.route('/fritos/<int:id>', methods=['GET'])
def fritosById(id):
    try:
        frito = Frito.query.filter_by(id=id).first()
        if frito != None:
            return jsonify({
                "id": frito.id,
                "nombre": frito.name,
                "precio": frito.precio
            })
        else:
            return jsonify({"mensaje": "frito no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al buscar frito"})
    
@fritos.route('/fritos', methods=['POST'])
def registrar_frito():
    try:
        nombre = request.json['nombre']
        precio = request.json['precio']

        frito = Frito(nombre, precio)
        db.session.add(frito)
        db.session.commit()
        return jsonify({"mensaje": "frito registrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al registrar frito"})
    
@fritos.route('/fritos/<int:id>', methods=['PUT'])
def actualizar_frito(id):
    try:
        frito = Frito.query.filter_by(id=id).first()
        if frito != None:
            nombre = request.json['nombre']
            precio = request.json['precio']

            frito.name = nombre
            frito.precio = precio
            db.session.commit()
            return jsonify({"mensaje": "frito actualizado"})
        else:
            return jsonify({"mensaje": "frito no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al actualizar frito"})
    
@fritos.route('/fritos/<int:id>', methods=['DELETE'])
def eliminar_frito(id):
    try:
        frito = Frito.query.filter_by(id=id).first()
        if frito != None:
            db.session.delete(frito)
            db.session.commit()
            return jsonify({"mensaje": "frito eliminado"})
        else:
            return jsonify({"mensaje": "frito no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al eliminar frito"})
    
