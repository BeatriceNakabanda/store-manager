# Product Queries
def check_product_exists(product_name):
    return """
            SELECT product_name FROM products WHERE product_name = '{}'
            """.format(product_name)

def insert_product(product_name, price, quantity):
    return """
            INSERT INTO products(product_name, price, quantity) 
                VALUES ('{}','{}','{}')
        """.format(product_name, price, quantity)

def fetch_products(product_name, price, quantity):
    return """
            SELECT product_name, price, quantity FROM products
        """

def fetch_one_product(product_id):
    return """
                SELECT product_name, price, quantity FROM products 
                WHERE product_id='{}'
        """.format(product_id)

def update_product(price, quantity, product_id):
    return """
                UPDATE products 
                SET price = '{}', quantity = '{}' 
                WHERE product_id = '{}'  
        """.format(price, quantity, product_id)

def check_item_exits(product_id):
    return """
                SELECT product_id FROM products WHERE product_id = '{}'
        """.format(product_id)

def delete_product(product_id):
    return """
            DELETE FROM products WHERE product_id = '{}'
        """.format(product_id)

# Sales Queries
def check_product(product_id):
    return """
                SELECT price, quantity FROM products WHERE product_id = '{}'
        """.format(product_id)

def make_sale(product_id, user_id, quantity, total):
    return """
                INSERT INTO sales(product_id, user_id, quantity, total) 
                VALUES ('{}','{}','{}','{}')
        """.format(product_id, user_id, quantity, total)

def update_products(new_quantity, product_id):
    return """
                UPDATE products SET quantity = {}
                WHERE product_id = {}
            """.format('new_quantity', product_id)

def get_sales(sale_id, product_id, user_id, quantity):
    return """
                SELECT sale_id, product_id, user_id, quantity total FROM sales
        """

def get_sale(sale_id):
        return """
                SELECT user_id, quantity, total FROM sales 
                WHERE sale_id='{}'
        """.format(sale_id)

# def delete_sale(sale_id):
#         return """
#             DELETE FROM sales WHERE sale_id = '{}'
#         """.format(sale_id)

# def check_sale(sale_):
#         return """
#                 SELECT sale_id FROM products WHERE sale_id = '{}'
#         """.format(sale_id)

# User Queries
def add_user(username, email, password):
        return """
                 INSERT INTO users(username, email, password) VALUES ('{}','{}','{}')
        """.format(username, email, password)

def get_user(username):
        return """
                SELECT username, password FROM users WHERE username='{}'
        """.format(username)