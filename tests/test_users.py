from .base import BaseTest
import json


class TestUser(BaseTest):
    sample_user = dict(
        username = "Juliet",
        email = "may@gmail.com",
        password = "123martha"
    )
    invalid_username = dict(
        username = 1826532341,
        email = "que@gmail.com",
        password = "123martha"
    )
    empty_inputs = dict(
        username = "",
        email = "",
        password = ""
    )
    invalid_email_format = dict(
        username = "Bright",
        email = "bright.com",
        password = "bright"
    )
    def test_create_user(self):
        with self.app.app_context():

            request = self.test_client.post(
                "/auth/signup",
                data = json.dumps(self.sample_user),
                content_type = "application/json"
            )
            print(request.data)
        self.assertIn(b'Username or password should have more than 8 characters', request.data)

    def test_empty_user_inputs(self):
        with self.app.app_context():

            request = self.test_client.post(
                "/auth/signup",
                data = json.dumps(self.empty_inputs),
                content_type = "application/json"
            )
            print(request.data)
        self.assertIn(b'Fill in all fields', request.data)

    def test_invalid_email_format(self):
        with self.app.app_context():

            request = self.test_client.post(
                "/auth/signup",
                data = json.dumps(self.invalid_email_format),
                content_type = "application/json"
            )
            print(request.data)
        self.assertIn(b'Invalid email format', request.data)