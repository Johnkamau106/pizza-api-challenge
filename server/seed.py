from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

def seed_data():
    with app.app_context():
        # Create tables
        db.drop_all()
        db.create_all()

        # Seed Restaurants
        restaurant1 = Restaurant(name="Pizza inn", address="123 Kenyatta ave")
        restaurant2 = Restaurant(name="Lennz House", address="456 Moi Ave")
        

        # Seed Pizzas
        pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Mashrooms")
        pizza2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Chicken")
        
        db.session.add_all([restaurant1, restaurant2, pizza1, pizza2])
        db.session.commit()

        # Seed Restaurant-Pizza relationships
        restaurant_pizza1 = RestaurantPizza(price=10.99, restaurant_id=restaurant1.id, pizza_id=pizza1.id)
        restaurant_pizza2 = RestaurantPizza(price=12.99, restaurant_id=restaurant1.id, pizza_id=pizza2.id)

        db.session.add_all([restaurant_pizza1, restaurant_pizza2 ])
        db.session.commit()

        print("Database seeded successfully!")
        
        