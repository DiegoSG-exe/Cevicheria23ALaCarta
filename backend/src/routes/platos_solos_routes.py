from flask import Blueprint, request, jsonify
from src.models import db
from src.models.models import Plato_Solo

platos_solos = Blueprint('platos_solos', __name__)

@platos_solos.route('/platos_solos', methods=['GET'])
def platosSolos():
    try:
        platos = Plato_Solo.query.all()
        platos_json = []
        for plato in platos:
            platos_json.append({
                "id": plato.id,
                "nombre": plato.name,
                "precio": plato.precio
            })
        if platos_json != []:
            return jsonify(platos_json)
        else:
            return jsonify({"mensaje": "no hay platos"})
    except Exception as e:
        return jsonify({"mensaje": "error al buscar platos"})
    
@platos_solos.route('/platos_solos/<int:id>', methods=['GET'])
def platosSolosById(id):
    try:
        plato = Plato_Solo.query.filter_by(id=id).first()
        if plato != None:
            return jsonify({
                "id": plato.id,
                "nombre": plato.name,
                "precio": plato.precio
            })
        else:
            return jsonify({"mensaje": "plato no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al buscar plato"})
    
@platos_solos.route('/platos_solos', methods=['POST'])
def registrar_plato():
    try:
        nombre = request.json['nombre']
        precio = request.json['precio']

        plato = Plato_Solo(nombre, precio)
        db.session.add(plato)
        db.session.commit()
        return jsonify({"mensaje": "plato registrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al registrar plato"})
    
@platos_solos.route('/platos_solos/<int:id>', methods=['PUT'])
def actualizar_plato(id):
    try:
        plato = Plato_Solo.query.filter_by(id=id).first()
        if plato != None:
            nombre = request.json['nombre']
            precio = request.json['precio']

            plato.name = nombre
            plato.precio = precio
            db.session.commit()
            return jsonify({"mensaje": "plato actualizado"})
        else:
            return jsonify({"mensaje": "plato no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al actualizar plato"})
    
@platos_solos.route('/platos_solos/<int:id>', methods=['DELETE'])
def eliminar_plato(id):
    try:
        plato = Plato_Solo.query.filter_by(id=id).first()
        if plato != None:
            db.session.delete(plato)
            db.session.commit()
            return jsonify({"mensaje": "plato eliminado"})
        else:
            return jsonify({"mensaje": "plato no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al eliminar plato"})
    