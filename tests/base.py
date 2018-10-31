from database.db import Database
import unittest
from api import app


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.test_client = app.test_client(self)
        self.db_con = Database()

    def tearDown(self):
        self.db_con.delete_table("products")
        self.db_con.delete_table("users")