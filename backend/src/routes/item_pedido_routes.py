from flask import Blueprint, request, jsonify
from src.models import db
from src.models.models import Items_Pedido, Plato, Pedido

items_pedido = Blueprint('items_pedido', __name__)

@items_pedido.route('/items_pedido', methods=['GET'])
def listItems_Pedido():
    try:
        items_pedido = Items_Pedido.query.all()
        items_pedido_json = []
        for item_pedido in items_pedido:
            items_pedido_json.append({
                "id": item_pedido.id,
                "cantidad": item_pedido.cantidad,
                "sub_total": item_pedido.sub_total,
                # "plato": item_pedido.plato,
                # "pedido": item_pedido.pedido
            })
        if items_pedido_json != []:
            return jsonify(items_pedido_json)
        else:
            return jsonify({"mensaje": "no hay items_pedido"})
    except Exception as e:
        return jsonify({"mensaje": "error al buscar items_pedido"})
    
@items_pedido.route('/items_pedido/<int:id>', methods=['GET'])
def items_pedidoById(id):
    try:
        item_pedido = Items_Pedido.query.filter_by(id=id).first()
        if item_pedido != None:
            return jsonify({
                "id": item_pedido.id,
                "cantidad": item_pedido.cantidad,
                "sub_total": item_pedido.sub_total,
                "plato": item_pedido.plato,
                "pedido": item_pedido.pedido
            })
        else:
            return jsonify({"mensaje": "item_pedido no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al buscar item_pedido"})
    
@items_pedido.route('/items_pedido', methods=['POST'])
def registrar_item_pedido():
    try:
        cantidad = request.json['cantidad']
        sub_total = request.json['sub_total']
        plato_id = request.json['plato_id']
        
        plato = Plato.query.filter_by(id=plato_id).first()

        pedido_id = request.json['pedido_id']

        pedido = Pedido.query.filter_by(id=pedido_id).first()

        item_pedido = Items_Pedido(cantidad, sub_total, plato, pedido)
        db.session.add(item_pedido)
        db.session.commit()
        return jsonify({"mensaje": "item_pedido registrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al registrar item_pedido"})
    
@items_pedido.route('/items_pedido/<int:id>', methods=['PUT'])
def actualizar_item_pedido(id):
    try:
        item_pedido = Items_Pedido.query.filter_by(id=id).first()
        if item_pedido != None:
            cantidad = request.json['cantidad']
            sub_total = request.json['sub_total']
            plato = request.json['plato']

            item_pedido.cantidad = cantidad
            item_pedido.sub_total = sub_total
            item_pedido.plato = plato

            db.session.commit()
            return jsonify({"mensaje": "item_pedido actualizado"})
        else:
            return jsonify({"mensaje": "item_pedido no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al actualizar item_pedido"})
    
@items_pedido.route('/items_pedido/<int:id>', methods=['DELETE'])
def eliminar_item_pedido(id):
    try:
        item_pedido = Items_Pedido.query.filter_by(id=id).first()
        if item_pedido != None:
            db.session.delete(item_pedido)
            db.session.commit()
            return jsonify({"mensaje": "item_pedido eliminado"})
        else:
            return jsonify({"mensaje": "item_pedido no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al eliminar item_pedido"})
    
@items_pedido.route('/items_pedido/upload', methods=['PUT'])
def upload_item_pedido():
    try:
        list_items = request.json['items']
        for item in list_items:
            item_pedido = Items_Pedido.query.filter_by(id=item['id']).first()
            if item_pedido != None:
                item_pedido.cantidad = item['cantidad']
                item_pedido.sub_total = item['sub_total']
                db.session.commit()
                return jsonify({"mensaje": "item_pedido actualizado"})
            else:
                return jsonify({"mensaje": "item_pedido no encontrado"})
    except Exception as e:
        return jsonify({"mensaje": "error al actualizar item_pedido"})