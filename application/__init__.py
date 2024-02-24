from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_migrate import upgrade
from flask_moment import Moment
from application.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config) 

    from application.public.views import public
    app.register_blueprint(public)


    return app