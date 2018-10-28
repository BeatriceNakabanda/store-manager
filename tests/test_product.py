import unittest
from api.models import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Shirt", 1, 1, 2000)

    def test_product_quantity_type(self):
        self.assertIsInstance(self.product.quantity, int)
        self.assertNotIsInstance(self.product.quantity, str)

    def test_price_datatype(self):
        self.assertIsInstance(self.product.price, int)
        self.assertNotIsInstance(self.product.price, float)
        self.assertNotIsInstance(self.product.price, str)

    def test_class_instance(self):
        self.assertIsInstance(self.product, Product)

