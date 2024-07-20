from django.db import models


class City(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return (self.name)

class Street(models.Model):
    name = models.CharField(max_length=40, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)

class Shop(models.Model):
    name = models.CharField(max_length=40, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.IntegerField(blank=False)
    opening = models.TimeField(blank=True)
    closing = models.TimeField(blank=True)

    def __str__(self):
        return (self.name)
