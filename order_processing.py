import os
import subprocess
import pickle
import hashlib
import yaml
import sqlite3

# Hardcoded credentials
DB_URL = "postgresql://admin:SuperSecret@123@prod.company.com:5432/orders"
STRIPE_KEY = "sk_live_4xKj9mN2pQ8rT5vW"
JWT_SECRET = "my-jwt-secret-key"

class OrderProcessor:

    def __init__(self):
        self.conn = sqlite3.connect("orders.db")

    def get_order(self, order_id):
        query = "SELECT * FROM orders WHERE id = " + order_id
        return self.conn.execute(query)

    def search_orders(self, customer_name):
        sql = "SELECT * FROM orders WHERE customer = '" + customer_name + "'"
        return self.conn.execute(sql)

    def filter_by_status(self, status):
        q = "SELECT * FROM orders WHERE status = '" + status + "'"
        return self.conn.execute(q)

    def verify_user(self, username, password):
        hashed = hashlib.md5(password.encode()).hexdigest()
        query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + hashed + "'"
        return self.conn.execute(query)

    def run_invoice_script(self, invoice_id):
        os.system("python invoices/generate.py " + invoice_id)

    def send_notification(self, email):
        subprocess.call("sendmail " + email, shell=True)

    def load_shipping_config(self, config_file):
        with open(config_file) as f:
            return yaml.load(f.read())

    def restore_order_backup(self, backup_path):
        with open(backup_path, "rb") as f:
            return pickle.loads(f.read())

    def get_invoice_file(self, order_id):
        path = "/invoices/" + order_id + ".pdf"
        with open(path, "rb") as f:
            return f.read()

    def get_customer_data(self, customer_id):
        base_path = "/data/customers/"
        return open(base_path + customer_id).read()

    def reset_password(self, user_id, new_password):
        hashed = hashlib.md5(new_password.encode()).hexdigest()
        query = "UPDATE users SET password = '" + hashed + "' WHERE id = " + user_id
        self.conn.execute(query)
        self.conn.commit()
