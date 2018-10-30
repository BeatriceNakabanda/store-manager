import unittest
from api.models import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Shirt", 2000, 1)

    def test_product_quantity_type(self):
        self.assertIsInstance(self.product.quantity, int)
        self.assertNotIsInstance(self.product.quantity, str)

    def test_product_price(self):
        self.assertEqual(self.product.price, 1, "price must be 1")

    def test_price_datatype(self):
        self.assertIsInstance(self.product.price, int)
        self.assertNotIsInstance(self.product.price, float)
        self.assertNotIsInstance(self.product.price, str)

    def test_class_instance(self):
        self.assertIsInstance(self.product, Product)

    def test_product_id(self):
        self.assertEqual(self.product.product_id, 1, "product_id must be 1")
        self.product.product_id = 5
        self.assertEqual(self.product.product_id, 5, "product_id is now 5")
    
    def test_product_id_type(self):
        self.assertNotIsInstance(self.product.product_id, str)
        self.assertIsInstance(self.product.product_id, int)

    def test_product_quantity(self):
        self.assertEqual(self.product.quantity, 2000, "Quantity should be 2000")

    def test_product_name(self):
        self.assertEqual(self.product.product_name, "Shirt")
        self.product.product_name = "skirt"
        self.assertEqual(self.product.product_name, "skirt", "skirt")


