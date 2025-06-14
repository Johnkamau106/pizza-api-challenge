from server.app import db

class Pizza:
    __tablename__ = 'pizzas'
    id = db.column(db.Integer(),primary_key=True)
    name = db.column(db.string(50), nullable=False)
    ingridients = db.column(db.string(200), nullable=False)
    
    restaurant_pizzas = db.relationship("RestaurantPizza", backref="pizza")
