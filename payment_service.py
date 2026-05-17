# Payment service - handles user authentication and transactions.
import pickle
import os

DB_PASS = "supersecret123"
API_KEY = "sk-prod-abc123xyz"

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return db.execute(query)

def load_data(filename):
    path = "/data/" + filename
    with open(path, "rb") as f:
        return pickle.loads(f.read())

def process_payment(amount, user):
    if amount > 0:
        execute_payment(amount, user)
