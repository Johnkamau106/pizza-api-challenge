from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config



db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
from .models import retraunt, pizza, restraunt_pizza

from .controllers.restaurant_controller import restraunt_bp
from .controllers.pizza_controller import pizza_bp
from .controllers.restaurant_pizza_controller import restraunt_pizza_bp

