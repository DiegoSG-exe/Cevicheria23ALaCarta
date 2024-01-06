from flask import Blueprint, request, jsonify
from src.models import db
from src.models.models import Plato, Trio_Marino, Ingrediente

trio_marino = Blueprint('trio_marino', __name__)

@trio_marino.route('/trio_marino', methods=['GET'])
def trioMarino():
    try:
        trios = Trio_Marino.query.all()
        trios_json = []
        for trio in trios:
            ingredientes = []
            for ingrediente in trio.ingredientes:
                ingredientes.append(ingrediente.name)

            trios_json.append({
                "id": trio.id,
                "nombre": trio.name,
                "ingredientes": ingredientes,
                "precio": trio.precio
            })
        if trios_json != []:
            return jsonify(trios_json)
        else:
            return jsonify({"mensaje": "no hay trios"})
    except Exception as e:
        return jsonify({"mensaje": "error al buscar trios" + str(e)})

@trio_marino.route('/trio_marino/<int:id>', methods=['GET'])
def trioMarinoById(id):
    try:
        trio = Trio_Marino.query.filter_by(id=id).first()
        if trio != None:
            ingredientes = []
            for ingrediente in trio.ingredientes:
                ingredientes.append(ingrediente.name)

            return jsonify({
                "id": trio.id,
                "nombre": trio.name,
                "ingredientes": ingredientes,
                "precio": trio.precio
            })
        else:
            return jsonify({"mensaje": "trio no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al buscar trio"})

@trio_marino.route('/trio_marino', methods=['POST'])
def registrar_trioMarino():
    try:
        nombre = request.json['nombre']
        precio = request.json['precio']

        trio_marino = Trio_Marino(name = nombre, precio = precio)
        
        db.session.add(trio_marino)
        
        plato = Plato.query.order_by(Plato.id.desc()).first()

        ingredientes_nombres = request.json.get('ingredientes', [])
        for ingrediente_nombre in ingredientes_nombres:
            ingrediente = Ingrediente.query.filter_by(name=ingrediente_nombre).first()
            if ingrediente == None:
                ingrediente = Ingrediente(ingrediente_nombre)
                db.session.add(ingrediente)
            plato.ingredientes.append(ingrediente)

        db.session.commit()

        return jsonify({"mensaje": "trio registrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al registrar trio " + str(e)}), 400
    


@trio_marino.route('/trio_marino/<int:id>', methods=['PUT'])
def actualizar_trioMarino(id):
    try:
        trio = Trio_Marino.query.get(id)
        if trio != None:
            trio.name = request.json['nombre']
            trio.precio = request.json['precio']

            ingredientes_nombres = request.json.get('ingredientes', [])

            plato = Plato.query.filter_by(id=id).first()
            
            plato.ingredientes.clear()
            
            for ingrediente_nombre in ingredientes_nombres:
                ingrediente = Ingrediente.query.filter_by(name=ingrediente_nombre).first()
                if ingrediente == None:
                    ingrediente = Ingrediente(ingrediente_nombre)
                    db.session.add(ingrediente)
                plato.ingredientes.append(ingrediente)

            db.session.commit()
            return jsonify({"mensaje": "trio actualizado"})
        else:
            return jsonify({"mensaje": "trio no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al actualizar trio"})


@trio_marino.route('/trio_marino/<int:id>', methods=['DELETE'])
def eliminar_trioMarino(id):
    try:
        trio = Trio_Marino.query.get(id)
        if trio != None:
            db.session.delete(trio)
            db.session.commit()
            return jsonify({"mensaje": "trio eliminado"})
        else:
            return jsonify({"mensaje": "trio no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al eliminar trio"})
