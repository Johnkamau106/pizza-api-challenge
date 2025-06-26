# 🍕 Pizza Restaurant API

A RESTful API for managing restaurants, pizzas, and their relationships, built with Flask using the MVC pattern. 

---

## 🚀 Project Structure

```
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── restaurant.py
│   │   ├── pizza.py
│   │   └── restaurant_pizza.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   └── restaurant_pizza_controller.py
│   └── seed.py
├── migrations/
├── challenge-1-pizzas.postman_collection.json
└── README.md
```

---

## 🧰 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd pizza-api-challenge
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   pipenv install flask flask_sqlalchemy flask_migrate
   pipenv shell
   ```

3. **Set up the database**
   - By default, uses SQLite (`dev.db`).
   - To use another DB, set the `DATABASE_URL` environment variable in `server/config.py` or your `.env` file.

4. **Run migrations**
   ```bash
   export FLASK_APP=server/app.py
   flask db init       
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Seed the database**
   ```bash
   python -m server.seed
   ```

6. **Run the server**
   ```bash
   export FLASK_APP=server/app.py
   flask run --port=5002
   ```

---

## 🏠 Root Route (`/`)

When you open the site in your browser (e.g. http://localhost:5002/), you will see:
- A JSON list of all pizzas if the database has pizzas.
- If the database is empty, an example pizza is shown.

**Example (if database is empty):**
```json
[
  {
    "id": 1,
    "name": "Example Pizza",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  }
]
```
**Example (if database has pizzas):**
```json
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
```

---

## 🗂️ Models

### Restaurant
- `id`: integer, primary key
- `name`: string
- `address`: string
- **Relationships:** has many `RestaurantPizzas`

### Pizza
- `id`: integer, primary key
- `name`: string
- `ingredients`: string
- **Relationships:** has many `RestaurantPizzas`

### RestaurantPizza (Join Table)
- `id`: integer, primary key
- `price`: integer (must be between 1 and 30)
- `restaurant_id`: foreign key
- `pizza_id`: foreign key
- **Relationships:** belongs to `Restaurant` and `Pizza`
- **Cascade delete:** Deleting a restaurant deletes related `RestaurantPizzas`

---

## 🛠️ API Routes

### GET /restaurants/
Returns a list of all restaurants.

**Example Response:**
```json
[
  {"id": 1, "name": "Pizza Palace", "address": "123 Main St"},
  {"id": 2, "name": "Kiki's Pizza", "address": "456 Side Ave"}
]
```

---

### GET /restaurants/<id>
Returns details of a single restaurant and its pizzas.

**Example Response:**
```json
{
  "id": 1,
  "name": "Pizza Palace",
  "address": "123 Main St",
  "pizzas": [
    {"id": 1, "name": "Margherita", "ingredients": "Dough, Tomato Sauce, Cheese", "price": 10}
  ]
}
```
**If not found:**
```json
{"error": "Restaurant not found"}
```
Status: 404

---

### DELETE /restaurants/<id>
Deletes a restaurant and all related RestaurantPizzas.
- **Success:** Status 204 No Content
- **If not found:**
```json
{"error": "Restaurant not found"}
```
Status: 404



### GET /pizzas/
Returns a list of all pizzas.

**Example Response:**
```json
[
  {"id": 1, "name": "Margherita", "ingredients": "Dough, Tomato Sauce, Cheese"},
  {"id": 2, "name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"}
]
```

---

### POST /restaurant_pizzas/
Creates a new RestaurantPizza.

**Request Body:**
```json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

**Success Response:**
```json
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {"id": 1, "name": "Margherita", "ingredients": "Dough, Tomato Sauce, Cheese"},
  "restaurant": {"id": 2, "name": "Kiki's Pizza", "address": "456 Side Ave"}
}
```

**Error Response:**
```json
{"errors": ["Price must be between 1 and 30"]}
```
Status: 400 Bad Request

---

## 🧪 Validation Rules
- `price` in `RestaurantPizza` must be an integer between 1 and 30 (inclusive).
- All foreign keys must reference existing records.

---

## 🔎 Testing with Postman
1. Open Postman.
2. Click `Import` and select `challenge-1-pizzas.postman_collection.json`.
3. Use the collection to test all endpoints.
4. Check responses and status codes for correctness.

---

## 📝 Notes
- All endpoints require trailing slashes (`/`).
- Use the correct HTTP method for each endpoint.
- The API uses SQLite by default for easy local development.
- The root URL `/` always returns a JSON example if the database is empty, so you can see the API structure immediately.
