from rest_framework.test import APITestCase
from cars.models import Car

class CarApiResponseTest(APITestCase):
    def test_get_cars_response_if_empty(self):
        response = self.client.get('/cars/')
        self.assertEqual(response.status_code, 204)

    def test_get_cars_response_not_empty(self):
        Car.objects.create(make="Volkswagen", model="Golf")
        response = self.client.get('/cars/')
        self.assertEqual(response.status_code, 200)


    def test_post_cars_response(self):
        response = self.client.post(
            '/cars/',
            {
                'make': 'Volkswagen',
                'model': 'Golf'
            }
        )
        self.assertEqual(response.status_code, 201)

    def test_post_car_if_not_found_in_external_api(self):
        response = self.client.post(
            '/cars/',
            {
                'make': 'volkswagen',
                'model': 'golf'
            }
        )
        self.assertEqual(response.status_code, 204)


class CarAPIDeleteTests(APITestCase):
    def setUp(self) -> None:
        Car.objects.create(make="Volkswagen", model="Golf")
        Car.objects.create(make="Renault", model="Clio")
        Car.objects.create(make="BMW", model="M3")

    def test_delete_object(self):
        response = self.client.delete(
            "/cars/1",
        )
        self.assertEqual(response.status_code, 204)

    def test_delete_and_check(self):
        response = self.client.get('/cars/2')
        self.assertEqual(response.status_code, 200)

        self.client.delete(
            "/cars/2",
        )

        response = self.client.get('/cars/2')
        self.assertEqual(response.status_code, 404)

class PostRatingTest(APITestCase):
    def setUp(self) -> None:
        self.client.post(
            "/cars/",
            {
                "make": "Volkswagen",
                "model": "Golf"
            }
        )

    def test_good_request_rating_post(self):
        response = self.client.post(
            "/rate/",
            {
                "car_id": 1,
                "rating": 3
            }
        )
        self.assertEqual(response.status_code, 201)

    def test_bad_request_rating_post(self):
        response = self.client.post(
            "/rate/",
            {
                "car_id": 10,
                "rating": 5
            }
        )

        self.assertEqual(response.status_code, 400)

    def test_bad_rating_post(self):
        response = self.client.post(
            "/rate/",
            {
                "car_id": 10,
                "rating": 8
            }
        )
        self.assertEqual(response.status_code, 400)

class PopularCarsTest(APITestCase):
    def setUp(self) -> None:
        Car.objects.create(make="Volkswagen", model="Golf")
        Car.objects.create(make="Renault", model="Clio")
        Car.objects.create(make="BMW", model="M3")

        self.client.post(
            "/rate/",
            {
                "car_id": 1,
                "rating": 5
            }
        )

        self.client.post(
            "/rate/",
            {
                "car_id": 2,
                "rating": 5
            }
        )

        self.client.post(
            "/rate/",
            {
                "car_id": 2,
                "rating": 5
            }
        )

    def test_response(self):
        response = self.client.get('/popular/')
        self.assertEqual(response.status_code, 200)
