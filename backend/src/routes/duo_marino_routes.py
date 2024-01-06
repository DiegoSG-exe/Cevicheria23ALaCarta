from flask import Blueprint, request, jsonify
from src.models import db
from src.models.models import Duo_Marino, Ingrediente, Plato

duo_marino = Blueprint('duo_marino', __name__)

@duo_marino.route('/duo_marino', methods=['GET'])
def duoMarino():
    try:
        duos = Duo_Marino.query.all()
        duos_json = []
        for duo in duos:
            ingredientes = []
            for ingrediente in duo.ingredientes:
                ingredientes.append(ingrediente.name)

            duos_json.append({
                "id": duo.id,
                "nombre": duo.name,
                "ingredientes": ingredientes,
                "precio": duo.precio
            })
        if duos_json != []:
            return jsonify(duos_json)
        else:
            return jsonify({"mensaje": "no hay duos"})
    except Exception as e:
        return jsonify({"mensaje": "error al buscar duos"})

@duo_marino.route('/duo_marino/<int:id>', methods=['GET'])
def duoMarinoById(id):
    try:
        duo = Duo_Marino.query.filter_by(id=id).first()
        if duo != None:
            ingredientes = []
            for ingrediente in duo.ingredientes:
                ingredientes.append(ingrediente.name)

            return jsonify({
                "id": duo.id,
                "nombre": duo.name,
                "ingredientes": ingredientes,
                "precio": duo.precio
            })
        else:
            return jsonify({"mensaje": "duo no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al buscar duo"})

@duo_marino.route('/duo_marino', methods=['POST'])
def registrar_duoMarino():
    try:
        nombre = request.json['nombre']
        precio = request.json['precio']

        duo_marino = Duo_Marino(nombre, precio)

        db.session.add(duo_marino)

        plato = Plato.query.order_by(Plato.id.desc()).first()

        ingredientes_nombres = request.json.get('ingredientes', [])
        for ingrediente_nombre in ingredientes_nombres:
            ingrediente = Ingrediente.query.filter_by(name=ingrediente_nombre).first()
            if ingrediente == None:
                ingrediente = Ingrediente(ingrediente_nombre)
                db.session.add(ingrediente)
            plato.ingredientes.append(ingrediente)

        db.session.commit()

        return jsonify({"mensaje": "duo registrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al registrar duo"})

@duo_marino.route('/duo_marino/<int:id>', methods=['PUT'])
def actualizar_duoMarino(id):
    try:
        nombre = request.json['nombre']
        precio = request.json['precio']

        duo_marino = Duo_Marino.query.filter_by(id=id).first()

        if duo_marino != None:
            duo_marino.name = nombre
            duo_marino.precio = precio

            ingredientes_nombres = request.json.get('ingredientes', [])
            
            plato = Plato.query.filter_by(id=id).first()

            plato.ingredientes.clear()

            for ingrediente_nombre in ingredientes_nombres:
                ingrediente = Ingrediente.query.filter_by(name=ingrediente_nombre).first()
                if ingrediente == None:
                    ingrediente = Ingrediente(ingrediente_nombre)
                    db.session.add(ingrediente)
                    db.session.commit()
                plato.ingredientes.append(ingrediente)

            db.session.commit()

            return jsonify({"mensaje": "duo actualizado"})
        else:
            return jsonify({"mensaje": "duo no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al actualizar duo"})

@duo_marino.route('/duo_marino/<int:id>', methods=['DELETE'])
def eliminar_duoMarino(id):
    try:
        duo_marino = Duo_Marino.query.get(id)
        if duo_marino != None:
            db.session.delete(duo_marino)
            db.session.commit()
            return jsonify({"mensaje": "duo eliminado"})
        else:
            return jsonify({"mensaje": "duo no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al eliminar duo"})
    