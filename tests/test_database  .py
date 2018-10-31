from .base import BaseTest


class TestDatabase(BaseTest):
    def test_db_conection(self):
        self.assertTrue(self.db_con)
    