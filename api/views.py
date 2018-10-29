from flask import Blueprint, jsonify, request, make_response
from api.models import Product, Sales, Store_Attendant
from api.validate import Validate
from werkzeug.security import generate_password_hash


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

@product.route('/api/v1/products/<int:product_id>', methods=['PUT'])
# @Auth.auth_required
# def update_single_product(product_id):
#     req_data = request.get_json()
#     update = Product.get_dict(product_id)
#     if not update:
#         return custom_response({'error': 'Post not found'}, 404)
#     return custom_response
#         data = blogpost_schema.dump(post).data
#   if data.get('owner_id') != g.user.get('id'):
#     return custom_response({'error': 'permission denied'}, 400)
  
#   data, error = blogpost_schema.load(req_data, partial=True)
#   if error:
#     return custom_response(error, 400)
#   post.update(data)
  
#   data = blogpost_schema.dump(post).data
#   return custom_response(data, 200)

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

users = []

# @user.route('/api/v1/users', methods=['POST'])
# def register_user():
#     """ registers users"""
#     data = request.get_json()
#     validate_user = Validate()
#     is_valid = validate_user.validate_user(data)
#     for attendant in users:
#         if attendant.email == data['email']:
#             return "user already exists!", 400
#     try:
#         if is_valid == "is_valid":
#             employee_id = len(users)
#             employee_id += 1
#             hashed_password = generate_password_hash(data['password'], method='admin')
#             user = Store_Attendant(employee_id, data['employee_name'],data['gender'], data['email'], data['user_name'], hashed_password)
#             users.append(user)
#             return jsonify({"message": "Store attendant successfully registered"}), 201
#         return make_response(is_valid)
#     except KeyError:
#         return "Invalid key fields"
