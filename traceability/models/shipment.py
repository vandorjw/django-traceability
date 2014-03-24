from django.db import models
from django.core.urlresolvers import reverse
from traceability.models.customer import Customer
from traceability.models.location import Address


class Shipment(models.Model):
    date_shipped = models.DateField()
    customer = models.ForeignKey(Customer)
    address = models.ForeignKey(Address)
    invoice_number = models.IntegerField(unique=True)

    class Meta:
        app_label = 'traceability'
        ordering = ['date_shipped']

    def __str__(self):
        return "%s - %s" % (self.id, self.customer)

    def get_absolute_url(self):
        return reverse(
            'traceability:shipment:shipment_detail',
            args=[self.id], )
