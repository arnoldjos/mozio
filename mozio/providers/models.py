from django.db import models

# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    language = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.name)


class ServiceArea(models.Model):
    provider = models.ForeignKey("Provider", related_name="service_areas", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.FloatField(default=0)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name = "Service Area"
        verbose_name_plural = "Service Areas"

    def __str__(self):
        return "{0}".format(self.name)
