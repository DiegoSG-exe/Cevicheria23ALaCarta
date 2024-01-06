from flask import Blueprint, jsonify, request
from src.models import db
from src.models.models import Pedido, Items_Pedido

pedido = Blueprint('pedido', __name__)

@pedido.route('/pedido', methods=['POST'])
def add_pedido():
    try:
        nuevo_pedido = Pedido(total = 0.0, estado = "Pendiente", ubicacion = "")
        db.session.add(nuevo_pedido)
        db.session.commit()

        return jsonify({
            "id" : nuevo_pedido.id,
            "mensaje": "Pedido creado"
            }), 200
    
    except Exception as e:
        return jsonify({"mensaje": "Error al crear pedido"}), 500

@pedido.route('/pedido', methods=['GET'])
def get_pedido():
    try:
        pedidos = Pedido.query.all()
        pedidos_json = []
        for pedido in pedidos:
            items_pedido = []
            for item in pedido.items_pedido:
                items_pedido.append({
                    "id" : item.id,
                    "cantidad" : item.cantidad,
                    "sub_total" : item.sub_total
                })
            pedidos_json.append({
                "id": pedido.id,
                "total": pedido.total,
                "estado": pedido.estado,
                "ubicacion": pedido.ubicacion,
                "fecha": pedido.fecha,
                "items_pedido" : items_pedido
            })
        if pedidos_json != []:
            return jsonify(pedidos_json)
        else:
            return jsonify({"mensaje": "No hay pedidos"}), 404
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener pedidos"}), 500

@pedido.route('/pedido/<int:id>', methods=['GET'])
def get_pedido_by_id(id):
    try:
        pedido = Pedido.query.filter_by(id=id).first()
        
        if pedido != None:
            items_pedido = []
            for item in pedido.items_pedido:
                items_pedido.append ( { 
                    "id": item.id,
                    "cantidad": item.cantidad,
                    "sub_total": item.sub_total,
                    "plato":  {
                        "nombre" : item.plato.name,
                        "precio" : item.plato.precio,
                        "tipo" : item.plato.tipo,
                        "ingredientes" : [
                            ingrediente.name for ingrediente in item.plato.ingredientes
                        ]
                        }
                    
                })
            return jsonify({
                "id": pedido.id,
                "total": pedido.total,
                "estado": pedido.estado,
                "ubicacion": pedido.ubicacion,
                "fecha": pedido.fecha,
                "items": items_pedido
            })
        else:
            return jsonify({"mensaje": "Pedido no encontrado"}), 404
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener pedido"}), 500
    

@pedido.route('/pedido/<int:id>', methods=['PUT'])
def update_pedido(id):
    try:
        pedido = Pedido.query.filter_by(id=id).first()
        if pedido != None:
            total = request.json['total']
            estado = request.json['estado']
            ubicacion = request.json['ubicacion']

            pedido.total = total
            pedido.estado = estado
            pedido.ubicacion = ubicacion

            db.session.commit()
            return jsonify({"mensaje": "Pedido actualizado"}), 200
        else:
            return jsonify({"mensaje": "Pedido no encontrado"}), 404
    except Exception as e:
        return jsonify({"mensaje": "Error al actualizar pedido"}), 500


@pedido.route('/pedido/<int:id>', methods=['DELETE'])
def delete_pedido(id):
    try:
        pedido = Pedido.query.filter_by(id=id).first()
        if pedido != None:
            db.session.delete(pedido)
            db.session.commit()
            return jsonify({"mensaje": "Pedido eliminado"}), 200
        else:
            return jsonify({"mensaje": "Pedido no encontrado"}), 404
    except Exception as e:
        return jsonify({"mensaje": "Error al eliminar pedido"}), 500
    

