from .base import BaseTest
import json


class TestLogin(BaseTest):
    sample_login = dict(
        username = "Juliet",
        password = "123martha"
    )
    invalid_login = dict(
        username = "",
        password = ""
    )
    def test_user_login(self):
        request = self.test_client.post(
            "/auth/signup",
            data = json.dumps(self.sample_login),
            content_type = "application/json"
        )
        print(request.data)
        self.assertIn(b'Fill in all fields', request.data)

    def test_invalid_login(self):
        request = self.test_client.post(
            "/auth/signup",
            data = json.dumps(self.invalid_login),
            content_type = "application/json"
        )
        print(request.data)
        self.assertIn(b'Fill in all fields', request.data)
