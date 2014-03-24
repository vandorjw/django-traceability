from django.db import models
from django.contrib.auth.models import User
from traceability.models.location import Address


class Employee(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=20, blank=True)
    address = models.ForeignKey(Address)
    start_employment = models.DateField()
    end_employment = models.DateField(blank=True, null=True)
    
    class Meta:
        app_label = 'traceability'
        ordering = ('start_employment', )

    def __str__(self):
        return self.user.get_full_name()
