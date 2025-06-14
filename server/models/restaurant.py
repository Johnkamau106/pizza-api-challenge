from server.app import db

class Restraunt:
    __tablenme__ = 'restraunts'
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.string(50), nullable=False)
    address = db.column(db.string(100), nullable=False)


    RestrauntPizzas = db.relationship("RestrauntPizza", backref="restraunt")