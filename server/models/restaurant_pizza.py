from server.app import db

class Restraunt_Pizza():
    id = db.column(db.integer, primary_key=True)
    price = db.column(db.float, nullable=False)
    restraunt_id = db.column(db.integer, db.foreign_key("restraunt.id"), nullable=False)
    pizza_id = db.column(db.integer, db.foreign_key("piza.id"), nullable=False)



