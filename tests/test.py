from rest_framework.test import APITestCase
from cars.models import Car

class CarApiResponseTest(APITestCase):
    def test_get_cars_response_if_empty(self):
        response = self.client.get('/cars/')
        self.assertEqual(response.status_code, 204)

