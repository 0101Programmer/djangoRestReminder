from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from reminder_app.models import User


# Create your tests here.

class UserIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('reminder_app:user-list')

    def test_user_list_integration(self):
        # Create test data
        User.objects.create(name='John', email='john@mail.ru', password='password123', birthdate='2000-01-01',
                            avatar='static/media/avatars/cat_developer.jpg', created_at=timezone.now(),
                            updated_at=timezone.now())
        User.objects.create(name='Jane', email='jane@mail.ru', password='password123', birthdate='2000-01-01',
                            avatar='static/media/avatars/cat_developer.jpg', created_at=timezone.now(),
                            updated_at=timezone.now())

        # Send a GET request to the URL
        response = self.client.get(self.url)

        # Assert the response status code and content
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John')
        self.assertContains(response, 'Jane')
