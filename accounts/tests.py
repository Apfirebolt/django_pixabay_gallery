from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser


class AccountsTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

    def test_login(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'testuser@example.com',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_register(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpass',
            'password2': 'newpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(CustomUser.objects.filter(email='testuser@example.com').exists())