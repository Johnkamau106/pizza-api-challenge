import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:mysecret@localhost/pizza-api-challenge")