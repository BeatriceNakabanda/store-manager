import unittest
from api.models import User


class TestProduct(unittest.TestCase):
    def setUp(self):
        kwargs = {
            "user_id": 1,
            "user_name": "Ella Beatirce",
            "email": "beat@gmail.com",
            "gender": "female",
            "username": "Ella",
            "password": "admin",
            "role": "admin"
        }
        self.user = User(**kwargs)

    def test_user_id(self):
        # Tests that the employee_id is equal to the given id
        self.assertEqual(self.user.user_id, 1, "User_id must be 1")
        self.user.user_id = 2
        self.assertEqual(self.user.user_id, 2, "User_id is now 2")

    def test_user_id_type(self):
        # Tests the datatype of the employee id
        self.assertNotIsInstance(self.user.user_id, str)
        self.assertIsInstance(self.user.user_id, int)

    def test_user_email(self):
        # Tests that the email is equal to the given email
        self.assertEqual(self.user.email, "beat@gmail.com")

    def test_email_type(self):
        # Tests the datatype of the email
        self.assertIsInstance(self.user.email, str)
        self.assertNotIsInstance(self.user.email, int)

    def test_gender_attribute(self):
        # Tests that the gender is equal to the given gender
        self.assertEqual(self.user.gender, "female")

    def test_gender_datatype(self):
        # Tests the gender data type
        self.assertIsInstance(self.user.gender, str)
        self.assertNotIsInstance(self.user.gender, float)
        self.assertNotIsInstance(self.user.gender, int)

    def test_password(self):
        # Tests that the password is equal to the given password
        self.assertEqual(self.user.password, "admin")
        self.user.password = "nimda"
        self.assertEqual(self.user.password, "nimda", "password is now nimda")

    def test_role(self):
        # Tests that the role is equal to the given role
        self.assertEqual(self.user.role, 'admin')

    def test_class_instance(self):
        # Tests that the defined object is an instance of the User class
        self.assertIsInstance(self.user, User)