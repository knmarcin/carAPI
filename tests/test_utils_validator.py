from rest_framework.test import APITestCase
from utils.rating_validator import rating_validator
from rest_framework.exceptions import ValidationError


class ValidationTest(APITestCase):

    def test_validation_if_string(self):
        with self.assertRaises(ValidationError):
            rating_validator("Nice")

    def test_validation_if_too_much(self):
        with self.assertRaises(ValidationError):
            rating_validator(6)

    def test_validation_if_too_less(self):
        with self.assertRaises(ValidationError):
            rating_validator(0)

    def test_validation_max(self):
        self.assertEqual(rating_validator(5), 5)

    def test_validation_min(self):
        self.assertEqual(rating_validator(1), 1)

    def test_validation_float(self):
        with self.assertRaises(ValidationError):
            self.assertEqual(rating_validator(1.2), 1)
