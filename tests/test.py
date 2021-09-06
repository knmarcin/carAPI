from rest_framework.test import APITestCase
from cars.models import Car

class CarApiResponseTest(APITestCase):
    def test_get_cars_response_if_empty(self):
        response = self.client.get('/cars/')
        self.assertEqual(response.status_code, 204)

    def test_get_cars_response_not_empty(self):
        response = self.client.post(
            "/cars/",
            {
                "make": "Volkswagen",
                "model": "Golf"
            }
        )
        response = self.client.get('/cars/')
        self.assertEqual(response.status_code, 200)


    def test_post_cars_response(self):
        response = self.client.post(
            "/cars/",
            {
                "make": "Volkswagen",
                "model": "Golf"
            }
        )
        self.assertEqual(response.status_code, 201)

    def test_post_car_if_not_found_in_external_api(self):
        response = self.client.post(
            "/cars/",
            {
                "make": "volkswagen",
                "model": "golf"
            }
        )
        self.assertEqual(response.status_code, 204)


