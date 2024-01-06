from flask import Blueprint, request, jsonify
from src.models import db
from src.models.models import Sopa

sopas = Blueprint('sopas', __name__)

@sopas.route('/sopas', methods=['GET'])
def listSopas():
    try:
        sopas = Sopa.query.all()
        sopas_json = []
        for sopa in sopas:
            sopas_json.append({
                "id": sopa.id,
                "nombre": sopa.name,
                "precio": sopa.precio
            })
        if sopas_json != []:
            return jsonify(sopas_json)
        else:
            return jsonify({"mensaje": "no hay sopas"})
    except Exception as e:
        return jsonify({"mensaje": "error al buscar sopas"})
    
@sopas.route('/sopas/<int:id>', methods=['GET'])
def sopasById(id):
    try:
        sopa = Sopa.query.filter_by(id=id).first()
        if sopa != None:
            return jsonify({
                "id": sopa.id,
                "nombre": sopa.name,
                "precio": sopa.precio
            })
        else:
            return jsonify({"mensaje": "sopa no encontrada"})
    except Exception as e:
        return jsonify({"mensaje": "error al buscar sopa"})
    
@sopas.route('/sopas', methods=['POST'])
def registrar_sopa():
    try:
        nombre = request.json['nombre']
        precio = request.json['precio']

        sopa = Sopa(nombre, precio)
        db.session.add(sopa)
        db.session.commit()
        return jsonify({"mensaje": "sopa registrada"})
    except Exception as e:
        return jsonify({"mensaje": "error al registrar sopa"})
    
@sopas.route('/sopas/<int:id>', methods=['PUT'])
def actualizar_sopa(id):
    try:
        sopa = Sopa.query.filter_by(id=id).first()
        if sopa != None:
            nombre = request.json['nombre']
            precio = request.json['precio']

            sopa.name = nombre
            sopa.precio = precio
            db.session.commit()
            return jsonify({"mensaje": "sopa actualizada"})
        else:
            return jsonify({"mensaje": "sopa no encontrada"})
    except Exception as e:
        return jsonify({"mensaje": "error al actualizar sopa"})
    
@sopas.route('/sopas/<int:id>', methods=['DELETE'])
def eliminar_sopa(id):
    try:
        sopa = Sopa.query.filter_by(id=id).first()
        if sopa != None:
            db.session.delete(sopa)
            db.session.commit()
            return jsonify({"mensaje": "sopa eliminada"})
        else:
            return jsonify({"mensaje": "sopa no encontrada"})
    except Exception as e:
        return jsonify({"mensaje": "error al eliminar sopa"})

