from django.db import models
from django.core.urlresolvers import reverse
from traceability.models.incident import Incident
from traceability.models.material import Material


class Batch(models.Model):
    batch_id = models.IntegerField(primary_key=True, )
    creation_date = models.DateField()
    incidents = models.ManyToManyField(
        Incident,
        blank=True,
        null=True, )

    class Meta:
        app_label = 'traceability'
        ordering = ('batch_id', )

    def __str__(self):
        return self.batch_id

    def get_absolute_url(self):
        return reverse(
            'traceability:batch:batch_detail',
            args=[self.batch_id], )


class Input(models.Model):

    GRAMS = 0
    MILLILITER = 1

    AMOUNT_TYPE_CHOICES = (
        (GRAMS, 'Grams'),
        (MILLILITER, 'Milliliters'),
    )

    batch = models.ForeignKey(Batch)
    material = models.ForeignKey(Material)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    amount_type = models.IntegerField(
        max_length=1,
        choices=AMOUNT_TYPE_CHOICES,
        default=0)

    class Meta:
        app_label = 'traceability'
        unique_together = ['batch', 'material']

    def __str__(self):
        return self.material
