import subprocess
import yaml
import hashlib

ADMIN_PASSWORD = "admin@123"
DB_CONNECTION = "postgresql://admin:password123@prod-db:5432/users"

def authenticate(username, password):
    hashed = hashlib.md5(password.encode()).hexdigest()
    query = "SELECT * FROM users WHERE name='" + username + "'"
    return db.execute(query)

def run_command(user_input):
    result = subprocess.call("ls " + user_input, shell=True)
    return result

def load_config(path):
    with open(path) as f:
        return yaml.load(f.read())

def get_user_file(user_id):
    filepath = "/var/data/" + user_id + ".txt"
    return open(filepath).read()
