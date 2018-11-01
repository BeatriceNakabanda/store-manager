from .base import BaseTest
import json


class TestSales(BaseTest):
    sample_sale = dict(
        product_id = 1,
        user_id = 1,
        quantity = 1
    )
    def test_sale_creation(self):
        with self.app.app_context():

            request = self.test_client.post(
                "/api/v1/sales",
                data = json.dumps(self.sample_sale),
                content_type = "application/json"
            )
            print(request.data)
        self.assertIn(b'sale added',request.data)