from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from accounts.models import CustomUser
from gallery.models import Gallery


class GalleryAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email='test@gmail.com',username='testuser', password='testpass')
        self.gallery = Gallery.objects.create(
            name='Test Gallery', user_id=self.user)

    def test_gallery_list(self):
        response = self.client.get(reverse('api:gallery-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_gallery_detail(self):
        self.client.login(username='test@gmail.com', password='testpass')
        response = self.client.get(reverse('api:gallery-crud', args=[self.gallery.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Gallery')

    def test_gallery_create(self):
        self.client.login(username='test@gmail.com', password='testpass')
        data = {'name': 'New Gallery'}
        response = self.client.post(reverse('api:gallery-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Gallery.objects.count(), 2)

    def test_gallery_update(self):
        self.client.login(username='test@gmail.com', password='testpass')
        data = {'name': 'Updated Gallery'}
        response = self.client.put(reverse('api:gallery-crud', args=[self.gallery.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.gallery.refresh_from_db()
        self.assertEqual(self.gallery.name, 'Updated Gallery')

    def test_gallery_delete(self):
        self.client.login(username='test@gmail.com', password='testpass')
        response = self.client.delete(reverse('api:gallery-crud', args=[self.gallery.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Gallery.objects.count(), 0)