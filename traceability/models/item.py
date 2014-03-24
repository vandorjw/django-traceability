from datetime import date
from django.db import models
from django.core.urlresolvers import reverse
from traceability.models.batch import Batch
from traceability.models.incident import Incident
from traceability.models.shipment import Shipment
from traceability.managers.item import InventoryManager


class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    batch = models.ForeignKey(Batch)
    shipment = models.ForeignKey(Shipment, null=True, blank=True)
    incidents = models.ManyToManyField(Incident, blank=True, null=True)
    weight = models.DecimalField(
        max_digits=6, decimal_places=3, default=0)

    objects = models.Manager()
    inventory = InventoryManager()

    class Meta:
        app_label = 'traceability'
        ordering = ('item_id',)

    def __str__(self):
        return str(self.item_id)

    def get_absolute_url(self):
        return reverse(
            'traceability:item:item_detail',
            args=[self.item_id], )

    @property
    def item_age(self):
        created = Batch.objects.get(pk=self.batch_id).creation_date
        delta = date.today() - created
        return delta.days
