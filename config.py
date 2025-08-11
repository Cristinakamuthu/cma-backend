from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_jwt_extended import JWTManager

# Naming convention for database constraints
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# Initialize extensions (not bound to app yet)
db = SQLAlchemy(metadata=metadata)
bcrypt = Bcrypt()
migrate = Migrate()
api = Api()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.secret_key = 'super-secret-key-change-this' 
    

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///worshiphub.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    app.config['JWT_SECRET_KEY'] = 'super-jwt-secret-change-this' 
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600 

   
    app.json.compact = False

  
    db.init_app(app)
    bcrypt.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    return app
