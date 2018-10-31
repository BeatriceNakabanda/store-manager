from database.db import Database
from werkzeug.security import generate_password_hash, check_password_hash


db_conn = Database()


class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

class Product:
    def __init__(self):
        self.cursor = db_conn.cursor
    
    def create_product(self, product_name, price, quantity):
        response = None
        item_exists = """
                SELECT product_name FROM products WHERE product_name = '{}'
        """.format(product_name)
        self.cursor.execute(item_exists)
        row = self.cursor.fetchone()

        query = """
        INSERT INTO products(product_name, price, quantity) VALUES ('{}','{}','{}')
        """.format(product_name, price, quantity)
        if row is not None:
            response = {"message":"Product already exists"}

        else:
            try:
                self.cursor.execute(query)
                response = {"message":"Product added"}
            except Exception as error:
                response = {"message":"Failed to add product because{}".format(error)}
        return response

    def fetch_products(self):
        response = None
        query ="""
                SELECT product_name, price, quantity FROM products
        """
        self.cursor.execute(query)
        products = self.cursor.fetchall()

        if products is not None:
            response = {"message":products}
        else:
             response = {"message":"Failed to get products"} 
        return response  

    def fetch_single_product(self, product_id):
        response = None
        query = """
                SELECT product_name, price, quantity FROM products 
                WHERE product_id='{}'
        """.format(product_id)
        self.cursor.execute(query)
        product = self.cursor.fetchone()

        if product is not None:
            response = {"message":product}
        else: 
            response = {"message": "Fetch single product failed"}
        return response

    def update_product(self, product_id, price, quantity):
        response = None
        query = """
                UPDATE products 
                SET price = '{}', quantity = '{}' 
                WHERE product_id = '{}'  
        """.format(price, quantity, product_id)

        item_exists = """
                SELECT product_id FROM products WHERE product_id = '{}'
        """.format(product_id)
        
        self.cursor.execute(item_exists)
        item = self.cursor.fetchone()

        if item is not None:
            self.cursor.execute(query)
            response = {"message":"Product updated successfully"}
        
        if response:
            return response
        else:
            response = {"message":"Failed to update product"}
        return response

    def delete_product(self, product_id):
        response = None
        query = """
            DELETE FROM products WHERE product_id = '{}'
        """.format(product_id)
        item_exists = """
                SELECT product_id FROM products WHERE product_id = '{}'
        """.format(product_id)
        
        self.cursor.execute(item_exists)
        item = self.cursor.fetchone()

        if item is not None:
            self.cursor.execute(query)
            response = {"message":"Product deleted"}
        
        if response:
            return response
        else:
            response = {"message":"Failed to delete product"}
        return response

class Sales:
    def __init__(self, sale_id, product_name, price, quantity,
                 total):
        self.sale_id = sale_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.total = total

    def get_dict(self):
        dict = {
            "sale_id": self.sale_id,
            "product_name": self.product_name,
            "price": self.price,
            "quantity": self.quantity,
            "total": self.total,
        }
        
        return dict

class User(object):
    def __init__(self, **kwargs):
        self.cursor = db_conn.cursor

    def create_user(self, username, email, password):
        response = None
        password = generate_password_hash(password)
        query = """
                INSERT INTO users(username, email, password) VALUES ('{}','{}','{}')
        """.format(username, email, password)
        try:
            self.cursor.execute(query)
            response = {"message":"User Created"}
        except Exception as error:
            response = {"message": "Failed because {}".format(error)}
        return response

    def authenticate_user(self, username, password):
        response = None
        query = """
                SELECT username, password FROM users WHERE username='{}'
        """.format(username)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        password = check_password_hash(user['password'],password)

        if user is not None and password:
            response = {"message":"Successfully logged in"}
        else: 
            response = {"message": "Invalid login"}
        return response