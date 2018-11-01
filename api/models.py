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
        product_exists = """
                SELECT product_name FROM products WHERE product_name = '{}'
        """.format(product_name)
        
        self.cursor.execute(product_exists)
        row = self.cursor.fetchone()

        product_creation_query = """
                INSERT INTO products(product_name, price, quantity) 
                VALUES ('{}','{}','{}')
        """.format(product_name, price, quantity)
        if row is not None:
            response = {"message":"Product already exists"}

        else:
            try:
                self.cursor.execute(product_creation_query)
                response = {"message":"Product added"}
            except Exception as error:
                response = {"message":"Failed to add product because{}".format(error)}
        return response

    def fetch_products(self):
        response = None
        fetch_products_query ="""
                SELECT product_name, price, quantity FROM products
        """
        self.cursor.execute(fetch_products_query)
        products = self.cursor.fetchall()

        if products is not None:
            response = {"products":products}
        else:
             response = {"message":"Failed to get products"} 
        return response  

    def fetch_single_product(self, product_id):
        response = None

        single_product_query = """
                SELECT product_name, price, quantity FROM products 
                WHERE product_id='{}'
        """.format(product_id)

        self.cursor.execute(single_product_query)
        product = self.cursor.fetchone()

        if product is not None:
            response = {"product":product}
        else: 
            response = {"message": "Fetch single product failed"}
        return response

    def update_product(self, product_id, price, quantity):
        response = None

        update_product_query = """
                UPDATE products 
                SET price = '{}', quantity = '{}' 
                WHERE product_id = '{}'  
        """.format(price, quantity, product_id)

        product_exists = """
                SELECT product_id FROM products WHERE product_id = '{}'
        """.format(product_id)
        
        self.cursor.execute(product_exists)
        item = self.cursor.fetchone()

        if item is not None:
            self.cursor.execute(update_product_query)
            response = {"message":"Product updated successfully"}
        
        if response:
            return response
        else:
            response = {"message":"Failed to update product"}
        return response

    def delete_product(self, product_id):
        response = None

        delete_product_query = """
            DELETE FROM products WHERE product_id = '{}'
        """.format(product_id)

        item_exists = """
                SELECT product_id FROM products WHERE product_id = '{}'
        """.format(product_id)
        
        self.cursor.execute(item_exists)
        item = self.cursor.fetchone()

        if item is not None:
            self.cursor.execute(delete_product_query)
            response = {"message":"Product deleted"}
        
        if response:
            return response
        else:
            response = {"message":"Failed to delete product"}
        return response

class Sales:
    def __init__(self):
        self.cursor = db_conn.cursor
        
    def create_sales(self, product_id, user_id, quantity):
        response = None

        product_exists = """
                SELECT price, quantity FROM products WHERE product_id = '{}'
        """.format(product_id)
        self.cursor.execute(product_exists)
        row = self.cursor.fetchone()

        if not row:
            response = {"message":"Product does not exist"}

        else:
            try:
                total = quantity * row.get("price")
                new_quantity = row.get("quantity") - quantity
                
                sale_creation_query = """
                            INSERT INTO sales(product_id, user_id, quantity, total) 
                            VALUES ('{}','{}','{}','{}')
                """.format(product_id, user_id, quantity, total)

                update_product = """
                    UPDATE products SET quantity = {}
                    WHERE product_id = {}
                """.format(new_quantity, product_id)

                self.cursor.execute(sale_creation_query)
                self.cursor.execute(update_product)
                response = {"message":"Made sale"}
            except Exception as error:
                response = {"message":"Failed to make sale because{}".format(error)}
        return response

    def fetch_sales(self):
        response = None
        fetch_sales_query ="""
                SELECT product_id, user_id, quantity, total FROM sales
        """
        self.cursor.execute(fetch_sales_query)
        sales = self.cursor.fetchall()

        if sales is not None:
            response = {"sales":sales}
        else:
             response = {"message":"Failed to get sales"} 
        return response  

    def fetch_single_sale_record(self, sale_id):
        response = None
        get_one_sale_query = """
                SELECT user_id, quantity, total FROM sales 
                WHERE sale_id='{}'
        """.format(sale_id)
        self.cursor.execute(get_one_sale_query)
        sale = self.cursor.fetchone()

        if sale is not None:
            response = {"sale":sale}
        else: 
            response = {"message": "Fetch single sale record failed"}
        return response

    def delete_sale(self, sale_id):
        response = None
        delete_sale_query = """
            DELETE FROM sales WHERE sale_id = '{}'
        """.format(sale_id)
        sale_exists = """
                SELECT sale_id FROM products WHERE sale_id = '{}'
        """.format(sale_id)
        
        self.cursor.execute(sale_exists)
        record = self.cursor.fetchone()

        if record is not None:
            self.cursor.execute(delete_sale_query)
            response = {"message":"Sale record deleted"}
        
        if response:
            return response
        else:
            response = {"message":"Failed to delete sale record"}
        return response

class User(object):
    def __init__(self):
        self.cursor = db_conn.cursor

    def create_user(self, username, email, password):
        response = None
        password = generate_password_hash(password)
        create_user_query = """
                 INSERT INTO users(username, email, password) VALUES ('{}','{}','{}')
        """.format(username, email, password)
        try:
            self.cursor.execute(create_user_query)
            response = {"message":"User Created"}
        except Exception as error:
            response = {"message": "Failed because {}".format(error)}
        return response

    def authenticate_user(self, username, password):
        response = None
        get_user_query = """
                SELECT username, password FROM users WHERE username='{}'
        """.format(username)
        self.cursor.execute(get_user_query)
        user = self.cursor.fetchone()
        password = check_password_hash(user['password'],password)

        if user is not None and password:
            response = {"message":"Successfully logged in"}
        else: 
            response = {"message": "Invalid login"}
        return response