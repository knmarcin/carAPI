import json

import requests

class Connector():

    def __init__(self, car_make: str, car_model: str):
        self.car_make = car_make
        self.car_model = car_model

    def get_data(self):
        api_request = requests.get(
            f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{self.car_make}?format=json")
        data = json.loads(api_request.content)['Results']
        for car in data:
            if car["Model_Name"] == self.car_model:
                return car
        # return list(filter(lambda car: car["Model_Name"] == self.car_model, data["Results"]))