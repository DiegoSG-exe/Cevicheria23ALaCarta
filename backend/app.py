from flask import Flask
from src.routes import trio_marino, duo_marino, fritos, platos_solos, sopas, items_pedido, pedido
from src.models import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://upwoux2uzaucpfbq:55yjjLJo4pK6RQxCHADE@baugewftytwefyfta8mn-mysql.services.clever-cloud.com:3306/baugewftytwefyfta8mn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(trio_marino)
app.register_blueprint(duo_marino)
app.register_blueprint(fritos)
app.register_blueprint(platos_solos)
app.register_blueprint(sopas)
app.register_blueprint(items_pedido)
app.register_blueprint(pedido)

db.init_app(app)