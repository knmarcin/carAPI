from rest_framework.test import APITestCase
from utils import connector


class TestConnector(APITestCase):
    def setUp(self) -> None:
        self.data = connector.Connector(
            car_make="Volksvagen",
            car_model="Golf"
        ).get_data()

    def test_if_not_empty(self):
        self.assertNotEqual(self.data, "")
