from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

ingredientes_platos = db.Table(
    'ingredientes_platos',
    db.Column('platos_id', db.Integer, db.ForeignKey('platos.id'), primary_key=True),
    db.Column('ingrediente_id', db.Integer, db.ForeignKey('ingredientes.id'), primary_key=True)
)

class Plato(db.Model):
    __tablename__ = 'platos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    precio = db.Column(db.Float)
    tipo = db.Column(db.String(255))
    ingredientes = db.relationship('Ingrediente', secondary=ingredientes_platos, backref='platos')

    def __init__(self, name, precio, tipo):
        self.name = name
        self.precio = precio
        self.tipo = tipo

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)

    def __init__(self, name):
        self.name = name

class Trio_Marino(Plato):
    __tablename__ = 'trio_marino'
    id = db.Column(db.Integer, db.ForeignKey('platos.id'), primary_key=True)

    def __init__(self, name, precio):
        super().__init__(name, precio, "trio_marino")

class Duo_Marino(Plato):
    __tablename__ = 'duo_marino'
    id = db.Column(db.Integer, db.ForeignKey('platos.id'), primary_key=True)

    def __init__(self, name, precio):
        super().__init__(name, precio, "duo_marino")

class Frito(Plato):
    __tablename__ = 'fritos'
    id = db.Column(db.Integer, db.ForeignKey('platos.id'), primary_key=True)

    def __init__(self, name, precio):
        super().__init__(name, precio, "frito")

class Plato_Solo(Plato):
    __tablename__ = 'platos_solos'
    id = db.Column(db.Integer, db.ForeignKey('platos.id'), primary_key=True)

    def __init__(self, name, precio):
        super().__init__(name, precio, "plato_solo")

class Sopa(Plato):
    __tablename__ = 'sopas'
    id = db.Column(db.Integer, db.ForeignKey('platos.id'), primary_key=True)

    def __init__(self, name, precio):
        super().__init__(name, precio, "sopa")

class Items_Pedido(db.Model):
    __tablename__ = 'items_pedido'
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    sub_total = db.Column(db.Float)

    plato_id = db.Column(db.Integer, db.ForeignKey('platos.id'))
    plato = db.relationship('Plato', backref='items_pedido_plato')

    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'))
    pedido = db.relationship('Pedido', back_populates='items_pedido', cascade='all, delete-orphan', single_parent=True)

    def __init__(self, cantidad, sub_total, plato, pedido):
        self.cantidad = cantidad
        self.sub_total = sub_total
        self.plato = plato
        self.pedido = pedido

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Float)
    estado = db.Column(db.String(255))
    ubicacion = db.Column(db.String(255))
    fecha = db.Column(db.DateTime)

    items_pedido = db.relationship('Items_Pedido', back_populates='pedido', cascade='all, delete-orphan', single_parent=True)
    
    def __init__(self, total, estado, ubicacion):
        self.total = total
        self.estado = estado
        self.ubicacion = ubicacion
        self.fecha = datetime.now()


