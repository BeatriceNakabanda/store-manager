# import unittest
# from api.models import Sales


# class Test_Sales(unittest.TestCase):
#     def setUp(self):
#         # Creates an instance of the SaleRecord class
#         self.new_record = Sales(5, "bag", "30000", "5", "150000")
#         return self.new_record

#     def test_class_instance(self):
#         # Tests if the object is an instance of the class
#         self.assertIsInstance(self.new_record, Sales)

#     def test_sale_id(self):
#         # Tests that the id is equal to the given id
#         self.assertNotEqual(self.new_record.sale_id, 1)
#         self.assertNotEqual(self.new_record.sale_id, "str")
#         self.assertEqual(self.new_record.sale_id, 5)

#     def test_sale_id_data_type(self):
#         # Tests the data type of the id
#         self.assertNotIsInstance(self.new_record.sale_id, str)
#         self.assertNotIsInstance(self.new_record.sale_id, float)
#         self.assertIsInstance(self.new_record.sale_id, int)

#     def test_product_name(self):
#         # Tests the existence of the product name
#         self.assertEqual(self.new_record.product_name, "bag")
#         self.assertNotEqual(self.new_record.product_name, "skirt")

#     def test_sold_product_datatype(self):
#         # Tests the datatype of the sold product name
#         self.assertNotIsInstance(self.new_record.product_name, int)
#         self.assertNotIsInstance(self.new_record.product_name, float)
#         self.assertIsInstance(self.new_record.product_name, str)

#     def test_sold_product_price(self):
#         # Tests the given price
#         self.assertEqual(self.new_record.price, "30000")
#         self.new_record.price = "10000"
#         self.assertEqual(self.new_record.price, "10000",
#                          "Price has now changed to 10000")

#     def test_price_datatype(self):
#         # Tests the datatype of the selling price
#         self.assertNotIsInstance(self.new_record.price, int)
#         self.assertNotIsInstance(self.new_record.price, float)
#         self.assertIsInstance(self.new_record.price, str)

#     def test_product_quantity(self):
#         # Tests that the product_quantity is equal to the given quantity
#         self.assertEqual(self.new_record.quantity, "5")
#         self.assertNotEqual(self.new_record.quantity, "10")
#         self.assertNotEqual(self.new_record.quantity, "20")

#     def test_sold_pdt_quantity_datatype(self):
#         # Tests the datatype of the product quantity
#         self.assertNotIsInstance(self.new_record.quantity, int)
#         self.assertNotIsInstance(self.new_record.quantity, float)
#         self.assertNotIsInstance(self.new_record.quantity, list)
#         self.assertIsInstance(self.new_record.quantity, str)

#     def test_total(self):
#         # Tests that the total amount is the product of price and quantity
#         self.assertEqual(self.new_record.total, "150000")
#         self.assertNotEqual(self.new_record.total, "65")

#     def test_total_type(self):
#         # Tests the datatype of the total amount
#         self.assertNotIsInstance(self.new_record.total, int)
#         self.assertNotIsInstance(self.new_record.total, float)
#         self.assertIsInstance(self.new_record.total, str)

#     def test_get_dict_function_returns_a_dictionary(self):
#         # Tests that the function returns a dictionary
#             response = {
#                     "sale_id": 1,
#                     "product_name": "Pen",
#                     "price": "600",
#                     "quantity": 2,
#                     "total": "1200"
#                }
#             self.assertEqual(response['sale_id'], 1)
#             self.assertEqual(response['price'], '600')