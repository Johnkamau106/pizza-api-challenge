from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config




db = SQLAlchemy()
migrate = Migrate()


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['DEBUG'] = True  

    db.init_app(app)
    migrate.init_app(app, db)

    
    from .models import restaurant, pizza, restaurant_pizza


    from .controllers.restaurant_controller import restaurant_bp
    from .controllers.pizza_controller import pizza_bp
    from .controllers.restaurant_pizza_controller import restaurant_pizza_bp





    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    @app.route("/")
    def home():
        return {"message": "Welcome to the Pizza API!"}

    with app.app_context():
        print("Registered routes:")
        for rule in app.url_map.iter_rules():
            print(f"{rule.endpoint}: {rule}")        


    return app