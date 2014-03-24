from django.db import models
from django.core.urlresolvers import reverse
from traceability.models.incident import Incident
from traceability.models.supplier import Supplier


class MaterialType(models.Model):
    material_type = models.CharField(max_length=255, )

    class Meta:
        app_label = 'traceability'
        ordering = ('material_type', )
        
    def __str__(self):
        return self.material_type


class Material(models.Model):
    material_type = models.ForeignKey(MaterialType)
    material_supplier = models.ForeignKey(Supplier)
    material_id = models.CharField(max_length=255)
    purchase_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    incidents = models.ManyToManyField(Incident, blank=True, null=True)
    
    class Meta:
        app_label = 'traceability'
        ordering = ('material_type', 'material_id', )
        unique_together = ("material_type", "material_id", )

    def __str__(self):
        return '%s - %s' % (self.material_type, self.material_id)

    def get_absolute_url(self):
        return reverse(
            'traceability:material:material_detail',
            args=[self.id], )
