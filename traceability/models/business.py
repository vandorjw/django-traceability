from django.db import models
from traceability.models.location import Address


class Business(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address)
    phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)

    class Meta:
        app_label = 'traceability'
        abstract = True

    def __str__(self):
        return self.name
