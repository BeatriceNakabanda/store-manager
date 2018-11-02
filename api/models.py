from database.db import Database
from database.database_queries import (check_product_exists, insert_product,  
        fetch_products, fetch_one_product, update_product, check_item_exits,
        delete_product, check_product, get_sales, get_sale, add_user, get_user
        )
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
        check_if_product_exists_query = check_product_exists(product_name)
        self.cursor.execute(check_if_product_exists_query)
        row = self.cursor.fetchone()

        if row is not None:
            response = {"message":"Product already exists"}

        else:
            try:
                add_new_product = insert_product(product_name, price, quantity)
                self.cursor.execute(add_new_product)
                response = {"message":"Product added"}
            except Exception as error:
                response = {"message":"Failed to add product because{}".format(error)}
        return response

    def fetch_products(self):
        response = None
        fetch_all_products = fetch_products('product_name', 'price', 'quantity')
        self.cursor.execute(fetch_all_products)
        products = self.cursor.fetchall()

        if products is not None:
            response = {"products":products}
        else:
             response = {"message":"Failed to get products"} 
        return response  

    def fetch_single_product(self, product_id):
        response = None
        get_one_product = fetch_one_product(product_id)
        self.cursor.execute(get_one_product)
        product = self.cursor.fetchone()

        if product is not None:
            response = {"product":product}
        else: 
            response = {"message": "Product does not exist"}
        return response

    def update_product(self, price, quantity, product_id):
        response = None
        check_if_item_exists = check_item_exits(product_id)
        update_my_product = update_product(price, quantity, product_id)
        
        self.cursor.execute(check_if_item_exists)
        item = self.cursor.fetchone()

        if item is not None:
            self.cursor.execute(update_my_product)
            response = {"message":"Product updated successfully"}
        
        # if response:
        #     return response
        # else:
        #     response = {"message":"Failed to update product"}
        # return response
        # response = None
        # update_product_query = update_product(price, quantity, product_id)
        # product_exists = check_item_exits(product_id)
        
        # self.cursor.execute(product_exists)
        # item = self.cursor.fetchone()

        # if item is not None:
        #     self.cursor.execute(update_product_query)
        #     response = {"message":"Product updated successfully"}
        
        # if response:
        #     return response
        # else:
        #     response = {"message":"Failed to update product"}
        # return response

    def delete_product(self, product_id):
        response = None
        check_if_item_exists = check_item_exits(product_id)
        delete_single_product = delete_product(product_id)
        self.cursor.execute(check_if_item_exists)
        item = self.cursor.fetchone()

        if item is not None:
            self.cursor.execute(delete_single_product)
            response = {"message":"Product deleted"}
        if response:
            return response
        else:
            response = {"message":"Product not found"}
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
                current_quantity = row.get("quantity") 
                new_quantity = current_quantity - quantity
                
                if quantity > current_quantity:  
                    response = {"message": "Not enough products in stock"}
                    return response
                
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
            except Exception:
                response = {"message":"Cannot make sale"}
        return response

    def fetch_sales(self, sale_id, product_id, user_id, quantity):
        response = None
        fetch_sales_query = get_sales(sale_id, product_id, user_id, quantity)
        self.cursor.execute(fetch_sales_query)
        sales = self.cursor.fetchall()

        if sales is not None:
            response = {"sales":sales}
        else:
             response = {"message":"No sales records available"} 
        return response  

    def fetch_single_sale_record(self, sale_id):
        response = None
        get_one_sale_query = get_sale(sale_id)
        self.cursor.execute(get_one_sale_query)
        sale = self.cursor.fetchone()

        if sale is not None:
            response = {"sale":sale}
        else: 
            response = {"message": "No sale record found"}
        return response

class User(object):
    def __init__(self):
        self.cursor = db_conn.cursor

    def create_user(self, username, email, password):
        response = None
        password = generate_password_hash(password)
        create_user_query = add_user(username, email, password)
        try:
            self.cursor.execute(create_user_query)
            response = {"message":"User Created"}
        except Exception:
            response = {"message": "User exists, use another username / email address"}
        return response

    def authenticate_user(self, username, password):
        response = None
        get_user_query = get_user(username)
        self.cursor.execute(get_user_query)
        user = self.cursor.fetchone()
        password = check_password_hash(user['password'],password)

        if user is not None and password:
            response = {"message":"Successfully logged in"}
        else: 
            response = {"message": "Invalid login"}
        return response