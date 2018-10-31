from .base import BaseTest
import json


class TestProduct(BaseTest):
    sample_product = dict(
        product_name = "Sodax",
        price = 200,
        quantity = 2
    )
    invalid_product = dict(
        product_name = 2018,
        price = 200,
        quantity = 2
    )
    empty_product = dict(
        product_name = "",
        price = "",
        quantity = None
    )
    def test_product_creation(self):
        with self.app.app_context():

            request = self.test_client.post(
                "/api/v1/products",
                data = json.dumps(self.sample_product),
                content_type = "application/json"
            )
            print(request.data)
        self.assertIn(b'Product added',request.data)

    def test_invalid_products_name(self):
        with self.app.app_context():

            request = self.test_client.post(
                "/api/v1/products",
                data = json.dumps(self.invalid_product),
                content_type = "application/json"
            )
            print(request.data)
        self.assertIn(b'Product name cannot be an integer',request.data)

    def test_empty_product_values(self):
        with self.app.app_context():

            request = self.test_client.post(
                "/api/v1/products",
                data = json.dumps(self.empty_product),
                content_type = "application/json"
            )
            print(request.data)
        self.assertIn(b'Fill in all fields',request.data)