from django.db import models
from django.core.urlresolvers import reverse
from traceability.models.location import Address


class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address)
    phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)

    class Meta:
        app_label = 'traceability'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'traceability:customer:customer_detail',
            args=[self.id], )
