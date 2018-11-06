from .base import BaseTest
import json


class TestSales(BaseTest):
    sample_sale = dict(
        product_id = 1,
        user_id = 1,
        quantity = 1
    )
    empty_sale = dict(
        product_id = "",
        user_id = "",
        quantity = ""
    )
    invalid_sale = dict(
        quantity = "Green",
        price = "blue"
    )
    def test_sale_creation(self):
        with self.app.app_context():

            request = self.test_client.post(
                "/api/v1/sales",
                data = json.dumps(self.sample_sale),
                content_type = "application/json"
            )
            print(request.data)
        self.assertIn(b'Product does not exist',request.data)

    def test_single_sale_record(self):
        with self.app.app_context():
            request = self.test_client.get(
                "/api/v1/sales/1",
                data = json.dumps(self.sample_sale),
                content_type = "application/json"
                )
        print(request.data)
        self.assertIn(b'No sale record found',request.data)

    def test_invalid_products_quantity_price(self):
        with self.app.app_context():

            request = self.test_client.post(
                "/api/v1/sales",
                data = json.dumps(self.invalid_sale),
                content_type = "application/json")
        print(request.data)
        self.assertIn(b'Quantity cannot be less than zero',request.data)

    def test_empty_sale_values(self):
        with self.app.app_context():

            request = self.test_client.post(
                "/api/v1/sales",
                data = json.dumps(self.empty_sale),
                content_type = "application/json"
            )
            print(request.data)
        self.assertIn(b'Fill any empty field',request.data)
