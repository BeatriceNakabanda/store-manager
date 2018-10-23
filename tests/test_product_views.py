import unittest
from api import app
import json


class TestProductViews(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client

    def test_create_a_product(self):
        post_data = ({
            "product_name": "Vacuum cleaner",
            "price": "800",
            "quantity": "1"
        })
        response = self.client().post('/api/v1/products', content_type='application/json', data=json.dumps(post_data))
        self.assertEqual(response.status_code, 201)

    def test_fetch_all_products(self):
        response = self.client().get('/api/v1/products', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_one_product(self):
        response = self.client().get('/api/v1/products/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_one_product_id(self):
        response = self.client().get('/api/v1/products/0', content_type='application/json')
        self.assertEqual(response.status_code, 400)