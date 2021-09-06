from django.db import models
from django.db.models import Avg

class Car(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    avg_rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}"

class CarRate(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super(CarRate, self).save(*args, **kwargs)
        car = Car.objects.get(id=self.car_id.id)
        rating = CarRate.objects.filter(car_id=self.car_id.id)
        car.avg_rating = rating.aggregate(Avg('rating'))['rating__avg']
        car.save()




