class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

class Product:
    def __init__(self, product_id, product_name, price = int, quantity = int):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def get_dict(self):
        dict = ({
            "product_id": self.product_id,
            "product_name": self.product_name,
            "price": self.price,
            "quantity": self.quantity
        })    
        return dict

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
        self.user_id = kwargs['user_id']
        self.user_name = kwargs['user_name']
        self.email = kwargs['email']
        self.gender = kwargs['gender']
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.role = kwargs['role']


    



