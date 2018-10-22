class Category:
    def __init__(self, category_id, category_name, date_created,date_modified):
        self.category_id = category_id
        self.category_name = category_name
        self.date_created = date_created
        self.date_modified = date_modified

class Product:
    """Product class defines the product sold by the store"""
    def __init__(self, product_id, product_name, date_added, price = int, quantity = int):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.date_added = date_added

    def serialize(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "price": self.price,
            "quantity": self.quantity,
            "date_added": self.date_added,
            }

class Sales:
    def __init__(self, sale_id, product_name, price, quantity,
                 total_amount, date_added):
        self.sale_id = sale_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.total_amount = total_amount
        self.date_added = date_added

    def get_dict(self):
        dict = {
            "sale_id": self.sale_id,
            "product_name": self.product_name,
            "price": self.price,
            "quantity": self.quantity,
            "total_amount": self.total_amount,
            "date_added": self.date_added
        }
        
        return dict


class ShoppingCart:
    def __init__(self, cart_id, date_created):
        self.cart_id = cart_id
        self.date_created = date_created

class StoreEmployee(object):
    def __init__(self, employee_id, employee_name, gender, email):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.gender = gender
        self.email = email
        

class Store_Attendant(StoreEmployee):
    def __init__(self, employee_id, employee_name,  gender, email, attendantUser_name, attendant_password):
        super().__init__(employee_id, employee_name, gender, email )
        self.store_attendantUser_name = attendantUser_name
        self.store_attendant_password = attendant_password


class Admin(StoreEmployee):
    def __init__(self, employee_id, employee_name, gender, email, adminUser_name, admin_password):
        super().__init__(employee_id, employee_name, gender, email)
        self.adminUser_name = adminUser_name
        self.admin_password = admin_password


