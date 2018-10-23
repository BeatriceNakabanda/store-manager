import unittest
from api.models import Sales


class Test_Sales(unittest.TestCase):
    def setUp(self):
        self.new_record = Sales(5, "Pen", "500", "10", "5000")
        return self.new_record

    def test_if_class_is_instance(self):
        self.assertIsInstance(self.new_record, Sales)

    def test_sale_id(self):
        self.assertNotEqual(self.new_record.sale_id, 1)
        self.assertNotEqual(self.new_record.sale_id, "str")
        self.assertEqual(self.new_record.sale_id, 3)

    def test_sale_id_data_type(self):
        self.assertNotIsInstance(self.new_record.sale_id, str)
        self.assertNotIsInstance(self.new_record.sale_id, float)
        self.assertIsInstance(self.new_record.sale_id, int)

    def test_sold_product_name(self):
        self.assertEqual(self.new_record.product_name, "Phone")
        self.assertNotEqual(self.new_record.product_name, "Cell Phome")

    def test_sold_product_datatype(self):
        self.assertNotIsInstance(self.new_record.product_name, int)
        self.assertNotIsInstance(self.new_record.product_name, float)
        self.assertIsInstance(self.new_record.product_name, str)

    def test_sold_product_price(self):
        # Tests the given price
        self.assertEqual(self.new_record.price, "200")
        self.new_record.price = "300"
        self.assertEqual(self.new_record.price, "300",
                         "Price has now changed to 300")

    def test_sold_product_price_datatype(self):
        self.assertNotIsInstance(self.new_record.price, int)
        self.assertNotIsInstance(self.new_record.price, float)
        self.assertIsInstance(self.new_record.price, str)

    def test_sold_pdt_quantity(self):
        self.assertEqual(self.new_record.quantity, "2")
        self.assertNotEqual(self.new_record.quantity, "2")
        self.assertNotEqual(self.new_record.quantity, "22")

    def test_sold_pdt_quantity_datatype(self):
        self.assertNotIsInstance(self.new_record.quantity, int)
        self.assertNotIsInstance(self.new_record.quantity, float)
        self.assertNotIsInstance(self.new_record.quantity, list)
        self.assertIsInstance(self.new_record.quantity, str)

    def test_total_amount(self):
        self.assertEqual(self.new_record.total_amount, "4500")
        self.assertNotEqual(self.new_record.total_amount, "45")

    def test_total_amount_type(self):
        self.assertNotIsInstance(self.new_record.total_amount, int)
        self.assertNotIsInstance(self.new_record.total_amount, float)
        self.assertIsInstance(self.new_record.total_amount, str)
