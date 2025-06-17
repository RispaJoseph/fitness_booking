from django.test import TestCase
from rest_framework.test import APIClient
from .models import FitnessClass
from django.utils import timezone
from datetime import timedelta

class BookingAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.class1 = FitnessClass.objects.create(
            name="Yoga",
            instructor="Rob",
            total_slots=2,
            available_slots=2,
            date_time=timezone.now() + timedelta(days=1)
        )

    def test_get_classes(self):
        response = self.client.get('/api/classes/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_successful_booking(self):
        data = {
            "class_id": self.class1.id,
            "client_name": "Alice",
            "client_email": "alice@example.com"
        }
        response = self.client.post('/api/book/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_booking_with_no_slots(self):
        self.class1.available_slots = 0
        self.class1.save()
        data = {
            "class_id": self.class1.id,
            "client_name": "Bob",
            "client_email": "bob@example.com"
        }
        response = self.client.post('/api/book/', data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'No slots available')

    def test_get_bookings_by_email(self):
        self.client.post('/api/book/', {
            "class_id": self.class1.id,
            "client_name": "Alice",
            "client_email": "alice@example.com"
        }, format='json')
        response = self.client.get('/api/bookings/?email=alice@example.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
