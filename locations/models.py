from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(blank=False, max_length=32)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return str(self.name)


class Country(models.Model):
    name = models.CharField(blank=False, default='Iran', max_length=32)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return str(self.name)


class State(models.Model):
    name = models.CharField(blank=False, max_length=32)

    def __str__(self):
        return str(self.name)


class Location(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='countries')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='states')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cites')

    def __str__(self):
        return f'{self.country}, {self.city}, {self.state}'

