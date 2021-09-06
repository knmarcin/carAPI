from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    avg_rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}"

class CarRate(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE())
    rating = models.IntegerField(blank=True, null=True)