import os


class config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres@localhost/pizza-api-challenge")
    SQLALCHEMY_TRACK_MODIFICATIONS = False