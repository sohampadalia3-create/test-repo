import os
import subprocess
import sqlite3
import yaml
import pickle

# Database configuration
HOST = "db.company.internal"
PORT = 5432
USERNAME = "db_admin"
PASSWORD = "Inv3ntory@2024!"
API_SECRET = "sk-inventory-prod-9f2k3m"

class InventoryManager:
    
    def __init__(self):
        self.db = sqlite3.connect("inventory.db")
    
    def search_product(self, product_name):
        # Search by product name
        query = "SELECT * FROM products WHERE name = '" + product_name + "'"
        return self.db.execute(query)
    
    def get_product_by_id(self, product_id):
        sql = "SELECT * FROM inventory WHERE id = " + product_id
        return self.db.execute(sql)
    
    def filter_by_category(self, category):
        q = "SELECT * FROM products WHERE category = '" + category + "' ORDER BY name"
        return self.db.execute(q)

    def run_report(self, report_name):
        os.system("python reports/" + report_name)

    def generate_export(self, export_type):
        result = subprocess.call("export_tool --type " + export_type, shell=True)
        return result

    def load_config(self, config_path):
        with open(config_path) as f:
            return yaml.load(f.read())

    def restore_backup(self, backup_file):
        with open(backup_file, "rb") as f:
            return pickle.loads(f.read())

    def get_supplier_file(self, supplier_id):
        path = "/data/suppliers/" + supplier_id + "/info.txt"
        with open(path) as f:
            return f.read()

    def export_to_file(self, user_input):
        filename = "/exports/" + user_input + ".csv"
        with open(filename, "w") as f:
            f.write(self.get_all_products())
