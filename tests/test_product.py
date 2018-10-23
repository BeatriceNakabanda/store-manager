import unittest
from api.models import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, 2000, "Shirt","Tue")

    def test_product_id(self):
        self.assertEqual(self.product.product_id, 1, "product_id must be 1")
        self.product.product_id = 6
        self.assertEqual(self.product.product_id, 6, "product_id is now 6")

    def test_product_id_type(self):
        self.assertNotIsInstance(self.product.product_id, str)
        self.assertIsInstance(self.product.product_id, int)

    def test_product_quantity(self):
        self.assertEqual(self.product.quantity, 8, "Quantity is 8")

    def test_product_quantity_type(self):
        self.assertIsInstance(self.product.quantity, int)
        self.assertNotIsInstance(self.product.quantity, str)

    def test_product_price(self):
        self.assertEqual(self.product.price, 3000, "price is 3000")

    def test_price_datatype(self):
        self.assertIsInstance(self.product.price, int)
        self.assertNotIsInstance(self.product.price, float)
        self.assertNotIsInstance(self.product.price, str)

    def test_product_name(self):
        self.assertEqual(self.product.product_name, "Omo")
        self.product.product_name = "Nomi"
        self.assertEqual(self.product.product_name, "Nomi",
                         "product name is now Nomi")

    def test_class_instance(self):
        self.assertIsInstance(self.product, Product)
