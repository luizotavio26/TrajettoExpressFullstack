from flasgger import Swagger
from config import app,db
from controller.manifesto_carga_controller import manifesto_cargas_blueprint
from controller.cadastro_cliente_controller import cadastro_clientes_blueprint
from controller.cadastro_veiculos_controller import cadastro_veiculos_blueprint
from controller.motorista_controller import motoristas_blueprint
from flask_cors import CORS
import os

CORS(app)

swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "API - Sistema de Manifesto de Carga",
        "description": "Documentação da API de Manifestos, Clientes, Veículos e Motoristas",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": [
        "http"
    ],
})

app.register_blueprint(manifesto_cargas_blueprint)
app.register_blueprint(cadastro_clientes_blueprint)
app.register_blueprint(cadastro_veiculos_blueprint)
app.register_blueprint(motoristas_blueprint)

#Só para testes, exlcuir depois
@app.route("/login", methods=['GET'])
def tela_login():
    return render_template("login.html")

if __name__ == "__main__":
    with app.app_context():
        if app.config['DEBUG']:
            db.create_all()


    app.run(
        
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )
    
