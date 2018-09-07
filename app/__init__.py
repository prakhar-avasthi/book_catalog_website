#app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app(config_type): #dev, test, or prod
    flask = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    flask.config.from_pyfile(configuration)

    db.init_app(flask)
    bootstrap.init_app(flask)
    login_manager.init_app(flask)
    bcrypt.init_app(flask)

    from app.catalog import main
    flask.register_blueprint(main)

    from app.auth import authentication
    flask.register_blueprint(authentication)
    return flask