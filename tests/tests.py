import unittest
from api.validate import Validate
from api import app


class TestValidator(unittest.TestCase):
    """ Tests Product validators """

    def setUp(self):
        """Sets up the validator class """
        self.validate = Validate()

    def test_validate_product(self):
        data = {
            "product_name": "foods",
            "product_quantity": "4",
            "price": "5000",
        }
        self.assertEqual(self.validate.validate_product(data), "Valid")

    # If product name is empty, function should fail
    def test_empty_product_name(self):
        data = {
            "product_name": "",
            "product_quantity": "3",
            "price": "5000"
        }
        with app.app_context():
            self.assertEqual(self.validate.validate_product(data),
                             ("Enter Product name", 400))

        # Do tests fail when price is null
    def test_empty_product_price(self):
        data = {
            "product_name": "Nomi",
            "product_quantity": "3",
            "price": ""
        }
        with app.app_context():
            self.assertEqual(self.validate.validate_product(data),
                             ("Enter the price of the product"))
    # Do tests when quanitity is null
    def test_empty_product_quantity(self):
        data = {
            "product_name": "Omo",
            "quantity": "",
            "price": "250"
        }
        with app.app_context():
            self.assertEqual(self.validate.validate_product(data),
                             ("Enter the quantity of the product"))

    # Does price accept integers only
    def test_price_value(self):
        data = {
            "product_name": "Nomi",
            "product_quantity": "54",
            "price": "price"
        }
        with app.app_context():
            self.assertEqual(self.validate.validate_product(data),
                             ("price should contain integers only", 400))

    # Does product quantity only accepts strings
    def test_product_quantity_value(self):
        data = {
            "product_name": "Pencil",
            "quantity": "quantity",
            "price": "17000"
        }
        with app.app_context():
            self.assertEqual(self.validate.validate_product(data),
                             ("quantity should contain integers only", 400))

    # Does function complain when wrong key value is given
    def test_wrong_key_values(self):
        data = {
            "": "Pen",
            "quantity": "3",
            "price": "500"
             }
        with app.app_context():
            self.assertEqual(self.validate.validate_product(data), ("Invalid Key Fields"))