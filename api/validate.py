import re


class Validate:
    """This class contains validators for the different entries"""
    def validate_product(self, data):
        # Validates the product fields
        product_name = data['product_name']
        price = data['price']
        quantity = data['quantity']
        # total = data['total']
        try:
            if not product_name or not price or not quantity:
                return  "Fill in all fields", 400

            if product_name and not isinstance(product_name, str):
                return "Product name has to be a string", 400
            
            if price and not isinstance(price, int):
                return "Price has to be an integer", 400

            if quantity and not isinstance(quantity, int):
                return "Quantity has to be an integer", 400

            # if total and not isinstance(total, int):
            #     return "Total has to be an int", 400

            else:
                return "Valid"

        except KeyError:
            return "Invalid Key Fields"

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
