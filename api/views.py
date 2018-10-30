from flask import Blueprint, g, jsonify, request, make_response, redirect, url_for
from api.models import Product, Sales, User
from api.validate import Validate
from functools import wraps
# from flask_jwt_extended import(
#     jwt_required,
#     create_access_token,
#     get_jwt_identity
# )


product = Blueprint('product', __name__)
sale = Blueprint('sale', __name__)
user = Blueprint('user', __name__)

products = [ ]

@product.route('/')
def home():
    return ('Welcome to Store Manager'), 200

@product.route('/api/v1/products', methods=['POST'])
def create_product():
    """Creates a new product"""
    data = request.get_json()
    validate = Validate()
    valid = validate.validate_product(data)
    item = dict( 
            product_name = data['product_name'],
            price = data['price'],
            quantity = data['quantity']
            )
    try:
        if valid == "Valid":
            product_id = len(products)
            product_id += 1
            product = [item for item in products if item["product_name"] == data['product_name'] ]
            new_product = Product(product_id, data['product_name'],data['price'], data['quantity'])
            if len(product) == 0:
                products.append(new_product.__dict__)
                return jsonify({"message": "Product created successfully",
                "data" : {
                    "product_name":"",
                    "Price":"",
                    "quantity":""
                         }
            } ), 201
            else:
                return jsonify({"message": "Product already exits"} ), 400
        return make_response(valid)
    except ValueError:
                return jsonify({"message": "Invalid"}), 400

@product.route('/api/v1/products', methods=['GET'])
def fetch_products():
    """Fetches all the available products"""
    Products = [product for product in products]
    return jsonify({"Products": Products}), 200
                
@product.route('/api/v1/products/<int:product_id>', methods=['GET'])
def fetch_single_product(product_id):
    fetched_product = []
    if product_id != 0 and product_id <= len(products):
        product = products[product_id - 1]
        fetched_product.append(product)
        return jsonify({"Product": fetched_product}), 200
    return jsonify({"message": "Index out of range!"}), 400

@product.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id == 0 or product_id > len(products):
        return jsonify({"message": "Index out of range"}), 400
    for product in products:
        if product.product_id == product_id:
            products.remove(product)
    return jsonify({"message": "product successfully removed"}), 200

@product.route('/api/v1/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Updates a product"""
    if product_id == 0 or product_id > len(products):
        return jsonify({"message": "Index is out of range"}), 400
    data = request.get_json()
    for product in products:
        if int(product.product_id) == int(product_id):
            product.product_name = data['product_name']
            product.quantity == data['quantity']
            product.price = data['price']
            return jsonify({'message': "Product updated successfully"}), 200

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

# users = []
# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if g.user is None:
#             return redirect(url_for('login', next=request.url))
#         return f(*args, **kwargs)
#     return decorated_function

# @user.route('/auth/signup', methods=['GET', 'POST'])
# @login_required
# def signup():
#     pass

# @user.route('/api/v1/auth/login')
# @login_required
# def login_page():
#     pass



