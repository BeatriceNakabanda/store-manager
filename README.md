# store-manager
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store
Features

    Admin can add a product
    Admin or store attendant can get all products
    Admin or store attendant can get a specific product.
    Store attendant can add a sale order.
    Admin can get all sale order details.

API Endpoints
REQUEST 	ROUTE       	                FUNCTIONALITY
GET 	    /api/v1/products 	            Fetches all products
GET 	    api/v1/products/<product_id> 	Fetches a single product
GET     	api/v1/sales                	Fetches all sales records
GET     	api/v1/sales/<sales_id>     	Fetches a single sales record
POST    	api/v1/products             	Creates a product
POST    	api/v1/sales 	                Creates a sales order

Getting started with the app

Technologies used to build the application

    Python 3.5.2

    Flask

Installation

Create a new directory and initialize git in it. Clone this repository by running

$ git clone 

Create a virtual environment. For example, with virtualenv, create a virtual environment named venv using

$ Python3 -m venv venv

Activate the virtual environment

$ Source venv/bin/activate

Install the dependencies in the requirements.txt file using pip

$ pip install -r requirements.txt

Start the application by running

$ python run.py

Test your setup using postman REST-client

Link to Store Manager on Heroku
store-man
