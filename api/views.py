from flask import Blueprint, jsonify, request, make_response
from api.models import Product, Sales, Store_Attendant
from api.validate import Validate
from datetime import datetime
from werkzeug.security import generate_password_hash


product = Blueprint('product', __name__)
sale = Blueprint('sale', __name__)
user = Blueprint('user', __name__)

products = []

@product.route('/')
def home():
    return ('Welcome to Store Manager'), 200

@product.route('/api/v1/products', methods=['POST'])
def create_product():
    """Creates a new product"""
    data = request.get_json()
    validate = Validate()
    valid = validate.validate_product(data)
    try:
        if valid == "Valid":
            product_id = len(products)
            product_id += 1
            new_product = Product(product_id, data['product_name'],data['price'], data['quantity'])
            products.append(new_product)
            return jsonify({"message": "Product created successfully"}), 201
        return make_response(valid)
    except ValueError:
                return jsonify({"message": "Invalid"}), 400
                
                
@product.route('/api/v1/products', methods=['GET'])
def fetch_products():
    """Fetches all the available products"""
    Products = [product.serialize() for product in products]
    return jsonify({"Products": Products}), 200
                
@product.route('/api/v1/products/<int:product_id>', methods=['GET'])
def fetch_single_product(product_id):
    fetched_product = []
    if product_id != 0 and product_id <= len(products):
        product = products[product_id - 1]
        fetched_product.append(product.serialize())
        return jsonify({"Product": fetched_product}), 200
    return jsonify({"message": "Index out of range!"}), 400

sale = Blueprint('sale', __name__)

sales = []



@sale.route('/api/v1/sales', methods=['POST'])
def create_sale_record():
    """ Creates a new sale record"""
    data = request.get_json()
    validate = Validate()
    valid = validate.validate_product(data)
    try:
        if valid == "Valid":
            record_id = len(sales)
            record_id += 1
            total = int(data['price']) * int(data['quantity'])
            new_record = Sales(record_id, data['product_name'],
                                    data['price'],
                                    data['quantity'],
                                    str(total))
            sales.append(new_record)
            return jsonify({"message": "record created successfully"}), 201
        return jsonify({"message": "Invalid fields"}), 400
    except ValueError:
        return jsonify({"message": "Invalid"})


@sale.route('/api/v1/sales', methods=['GET'])
def fetch_sale_orders():
    """This endpoint fetches all sale records"""
    Sales = [record.get_dict() for record in sales]
    return jsonify({"All Sales": Sales}), 200


@sale.route('/api/v1/sales/<int:sale_id>', methods=['GET'])
def get_single_record(sale_id):
    single_record = []
    if sale_id != 0 and sale_id <= len(sales):
        record = sales[sale_id - 1]
        single_record.append(record.get_dict())
        return jsonify({"Record": single_record}), 200
    return jsonify({"message": "Index out of range!"}), 400

user = Blueprint('user', __name__)

users = []


@user.route('/api/v1/users', methods=['POST'])
def register_user():
    """ registers users"""
    data = request.get_json()
    validate_user = Validate()
    is_valid = validate_user.validate_user(data)
    for attendant in users:
        if attendant.email == data['email']:
            return "user already exists!", 400
    try:
        if is_valid == "is_valid":
            employee_id = len(users)
            employee_id += 1
            hashed_password = generate_password_hash(data['password'], method='admin')
            user = Store_Attendant(employee_id, data['employee_name'],data['gender'], data['email'], data['user_name'], hashed_password)
            users.append(user)
            return jsonify({"message": "Store attendant successfully registered"}), 201
        return make_response(is_valid)
    except KeyError:
        return "Invalid key fields"
