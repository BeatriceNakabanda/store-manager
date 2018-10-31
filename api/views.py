from flask import Blueprint, g, jsonify, request, make_response, redirect, url_for
from api.models import Product, Sales, User
from functools import wraps
import re


product = Blueprint('product', __name__)
sale = Blueprint('sale', __name__)
user = Blueprint('user', __name__)
user_object = User()
product_object = Product()

products = [ ]

@product.route('/')
def home():
    return ('Welcome to Store Manager'), 200

@product.route('/api/v1/products', methods=['POST'])
def create_product():
    # Creates a new product
    data = request.get_json()
    product_name = data.get("product_name")
    price = data.get("price")
    quantity = data.get("quantity")
    response = None
    if not product_name or not price or not quantity:
        response = "Fill in all fields"

    if product_name and not isinstance(product_name, str):
        response = "Product name cannot be an integer"

    if price and not isinstance(price, int):
        response = "Price cannot be a string"

    if quantity and not isinstance(quantity, int):
        response = "Quantity cannot be a string"

    if response:
        return jsonify(response)
    else:
        response = product_object.create_product(product_name, price, quantity)
    return jsonify(response)

@product.route('/api/v1/products', methods=['GET'])
def fetch_products():
    response = product_object.fetch_products()
    return jsonify(response) 
                
@product.route('/api/v1/products/<int:product_id>', methods=['GET'])
def fetch_single_product(product_id):
    response = product_object.fetch_single_product(product_id)
    return jsonify(response)
    
@product.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    response = product_object.delete_product(product_id)
    return jsonify(response)

@product.route('/api/v1/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Updates a product"""
    product_data = request.get_json()
    price = product_data.get("price")
    quantity = product_data.get("quantity")
    response = product_object.update_product(product_id, price, quantity)
    return jsonify(response)

sales = [] 

@sale.route('/api/v1/sales', methods=['POST'])
def create_sale_record():
    """ Creates a new sale record"""
    data = request.get_json()
    validate = Validate()
    valid = validate.validate_product(data)
    item = dict( 
            product_name = data['product_name'],
            price = data['price'],
            quantity = data['quantity'],
            total = data['total']
        )
    try:
        if valid == "Valid":
            record_id = len(sales)
            record_id += 1
            sale =[item for item in sales if item["product_name"] == data['product_name']]
            total = int(data['price']) * int(data['quantity'])
            new_record = Sales(record_id, data['product_name'],data['price'], data['quantity'],str(total))
            if len(sale) == 0:
                sales.append(new_record.__dict__)
                return jsonify({"message": "record created successfully", 
                "sales" : {
                    "product_name":"",
                    "Price":"",
                    "quantity":"",
                    "total": ""
                         }
                }), 201
            else:
                return jsonify({"message": "Product already exits"} ), 400
        return jsonify({"message": "Invalid fields"}), 400
    except ValueError:
        return jsonify({"message": "Invalid"})

@sale.route('/api/v1/sales', methods=['GET'])
def fetch_sale_orders():
    """This endpoint fetches all sale records"""
    Sales = [sale for sale in sales]
    return jsonify({"All Sales": Sales}), 200

@sale.route('/api/v1/sales/<int:sale_id>', methods=['GET'])
def get_single_record(sale_id):
    single_record = []
    if sale_id != 0 and sale_id <= len(sales):
        record = sales[sale_id - 1]
        single_record.append(record)
        return jsonify({"Record": single_record}), 200
    return jsonify({"message": "Index out of range!"}), 400

@user.route('/auth/signup', methods=['POST'])
def signup():
    user_data = request.get_json()
    username = user_data.get("username")
    email = user_data.get("email")
    password = user_data.get("password")
    response = None
    if not username or not email or not password:
        response = "Fill in all fields"

    if username and not isinstance(username, str):
        response = "Username cannot be an integer"
    
    if email and not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        response = "Invalid email format"

    if response:
        return jsonify(response)
    else:
        response = user_object.create_user(username, email, password)
    return jsonify(response)

@user.route('/api/v1/auth/login', methods=['POST'])
def login():
    login_data = request.get_json()
    username = login_data.get("username")
    password = login_data.get("password")
    response = None
    if not username or not password:
        response = "Fill in all fields"
    else:
        response = user_object.authenticate_user(username, password)
    return jsonify(response)