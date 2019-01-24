from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test creating a user with email address is test_create_user_with_email_successful
        """
        email = "testing@gmail.com"
        password = "Testing@1234"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Testing for the doamin name in an email address to be case insensitive
        """
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user( email, 'testing123')

        self.assertEqual(user.email, email.lower())
