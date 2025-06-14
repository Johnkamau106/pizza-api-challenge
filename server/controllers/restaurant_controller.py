from flask import Blueprint, jsonify, request
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import Restaurant_Pizza
from server.app import db

restaurant_bp = Blueprint('retaurant', __name__, url_prefix='/restaurants')

@restaurant_bp.route('/', methods=['GET'])

def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{"id": restaurant.id, "name": restaurant.name, "address": restaurant.address}])

@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        pizzas = []
        for rp in restaurant.restaurant_pizzas:
            pizzas.append({
                "id": rp.pizza.id,
                "name": rp.pizza.name,
                "ingredients": rp.pizza.ingredients,
                "price": rp.price
            })
        return jsonify({
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "pizzas": pizzas
        })
    else:
        return jsonify({"error": "Restaurant not found"}), 404
@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return jsonify({"message": "Restaurant deleted successfully"})
    else:
        return jsonify({"error": "Restaurant not found"}), 404
    