from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location_signup_view(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "test_user",
                "email": "test_user@example.com",
                "password1": "test_password",
                "password2": "test_password",
            },
        )
        self.assertEqual(response.status_code, 302)

        user = get_user_model().objects.all()[0]
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.email, "test_user@example.com")
