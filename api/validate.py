import re


class Validate:
    """This class contains validators for the different entries"""
    def validate_product(self, data):
        # Validates the product fields
        try:
            if data['product_name'] == "":
                return "Enter Product name", 400

            if data['price'] == "":
                return "Enter the price of the product", 400

            if data["quantity"] == "":
                return "Enter the product quantity", 400
            
            if data["quantity"] == "":
                return "Enter the product quantity", 400

            else:
                return "Valid"
        except KeyError:
            return "Invalid Key Fields"

               
        except KeyError:
                return "Invalid fields"


    def validate_user(self, data):
        # Validates user fields
        try:
            if len(data.keys()) == 0:
                return "No user added", 400

            if data['user_name'] == "":
                return "Fill in Username", 400

            if data['email'] == "":
                return "Fill in Emaill Address", 400

            if data['password'] == "":
                return "Fill in Password", 400

            if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)",
                            data['email']):
                return "Invalid email format", 400

            if len(data['password']) < 4:
                return "Password should have more than four characters ", 400
            else:
                return "is_valid"
        except KeyError:
            return "Invalid"
