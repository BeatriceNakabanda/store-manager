from flask import Flask
from api.models import User
import re


class Validate:
    """This class contains validators for the different entries"""
    def validate_product(self, data):
        # Validates the product fields
        product_name = data['product_name']
        price = data['price']
        quantity = data['quantity']
        try:
            if not product_name or not price or not quantity:
                return  "Fill in all fields", 400

            if product_name and not isinstance(product_name, str):
                return "Product name has to be a string", 400
            
            if price and not isinstance(price, int):
                return "Price has to be an integer", 400

            if quantity and not isinstance(quantity, int):
                return "Quantity has to be an integer", 400

            else:
                return "Valid"

        except KeyError:
            return "Invalid Key Fields"

            # # if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)",
            #                 data['email']):
            #     return "Invalid email format", 400

            # if len(data['password']) < 4:
            #     return "Password should have more than four characters ", 400
            
        except KeyError:
            return "Invalid"
