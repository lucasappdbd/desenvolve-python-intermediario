import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)

login = LoginManager(app)
app.config['SECRET_KEY'] = "PD12345678"

# app.secret_key = 'dev'

## Iniciando a conexão com o banco ##
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite+pysqlite:///microblog.db"
db = SQLAlchemy()
db.init_app(app) ## Cria uma pasta instance/ para o banco ##


from app import routes
from app.models import models
## Criando as tabelas em models ##
with app.app_context():
    db.create_all()

from app import alquimias
