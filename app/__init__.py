from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bootstrap import Bootstrap

db=SQLAlchemy()
bootstrap=Bootstrap()
def create_app(config_name):
    app=Flask(__name__)

    # Creating application configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extentions
    db.init_app(app)
    bootstrap.init_app(app)

    # Registering the blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


