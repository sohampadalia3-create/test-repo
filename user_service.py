import os
import pickle

DB_HOST = "prod-server"
DB_PASS = "mypassword456"    # similar to past hardcoded secret

def find_user(user_name):
    # similar to past SQL injection
    sql = "SELECT * FROM accounts WHERE username = '" + user_name + "'"
    return database.execute(sql)

def load_session(session_id):
    # similar to past pickle vulnerability
    data = redis.get(session_id)
    return pickle.loads(data)

def read_profile(user_id):
    file_path = "/profiles/" + user_id
    with open(file_path) as f:
        return f.read()
