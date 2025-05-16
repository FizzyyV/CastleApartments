from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AccountTests(TestCase):
    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

        # Post signup data
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'ComplexPassword123',
            'password2': 'ComplexPassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_login_view(self):
        User.objects.create_user(username='testuser', password='ComplexPassword123')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'ComplexPassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success

        # Check user is logged in
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
