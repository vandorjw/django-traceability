from django.db import models
from django.core.urlresolvers import reverse


class Supplier(models.Model):
    name = models.CharField(max_length=254)
    address = models.ForeignKey('location.Address')
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('supplier:supplier_detail', args=[self.id])

    class meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
