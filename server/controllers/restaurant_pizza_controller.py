from flask import Blueprint, request, jsonify
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.app import db

restaurant_pizza_bp = Blueprint('restaurant_pizza', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    try:
        price = float(data.get("price"))
        pizza_id = int(data.get("pizza_id"))
        restaurant_id = int(data.get("restaurant_id"))
    except (TypeError, ValueError):
        return jsonify({"errors": ["Invalid data types."]}), 400

    # Validation: price between 1 and 30
    if price < 1 or price > 30:
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
        return jsonify({"errors": ["Invalid restaurant or pizza ID"]}), 400

    restaurant_pizza = RestaurantPizza(
        price=price,
        pizza_id=pizza_id,
        restaurant_id=restaurant_id
    )

    db.session.add(restaurant_pizza)
    db.session.commit()

    return jsonify({
        "id": restaurant_pizza.id,
        "price": restaurant_pizza.price,
        "pizza_id": restaurant_pizza.pizza_id,
        "restaurant_id": restaurant_pizza.restaurant_id,
        "pizza": {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        },
        "restaurant": {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
    }), 201

