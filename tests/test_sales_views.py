import unittest
from api import app
from flask import json


class TestSaleViews(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client

    def test_create_a_sale(self):
        post_data = ({
            "product_name": "Pen",
            "price": "3550",
            "quantity": "2"
        })
        response = self.client().post('/api/v1/sales', content_type='application/json', data=json.dumps(post_data))
        self.assertEqual(response.status_code, 201)

    def test_fetch_all_sales(self):
        response = self.client().get('/api/v1/sales', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_a_single_record(self):
        response = self.client().get('/api/v1/sales/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_one_sale_id(self):
        response = self.client().get('/api/v1/sales/0', content_type='application/json')
        self.assertEqual(response.status_code, 400)