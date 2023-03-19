from django.db import models
from Divar import settings
from category.models import Category
from locations.models import Location


class Advertisement(models.Model):
    NEW = 1
    FRESH = 2

    ATTRIBUTE_TYPE_FIELDS = (
        (NEW, "New"),
        (FRESH, "Fresh"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='advertisements')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ad_category', verbose_name='Category')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='ad_location', verbose_name='Location')
    title = models.CharField(max_length=32, verbose_name='Title')
    description = models.TextField(blank=True, verbose_name='Description')
    price = models.IntegerField(default=0, verbose_name='Price')
    phone_number = models.CharField(verbose_name='Mobile Number', max_length=13)
    status = models.PositiveSmallIntegerField(default=NEW, choices=ATTRIBUTE_TYPE_FIELDS)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('adv-detail', args=[self.pk])

    def __str__(self):
        return f"{self.title} > {self.location.city.name}"


class AdvertisementImage(models.Model):
    image = models.ImageField(upload_to='advertisements/')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return str(self.advertisement)
