from flask import Flask, redirect
from api.views import product
from api.views import sale
from api.views import user

app = Flask(__name__)
app.register_blueprint(product)
app.register_blueprint(sale)
app.register_blueprint(user)


@app.route('/')
def index():
    return redirect('/')
