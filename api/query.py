
from database.db import Database

db_conn = Database()


data = {}
product_name = data.get("product_name")
price = data.get("price")
quantity = data.get("quantity")

# product queries
products = """ SELECT product_name FROM products 
        WHERE product_name = '{}' """.format(product_name)

creation = """ INSERT INTO products(product_name, price, quantity) 
                VALUES ('{}','{}','{}')
        """.format(product_name, price, quantity)