import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    if not SQLALCHEMY_DATABASE_URI:
        raise RuntimeError("DATABASE_URL environment variable must be set to a valid PostgreSQL URI.")
    SQLALCHEMY_TRACK_MODIFICATIONS = False