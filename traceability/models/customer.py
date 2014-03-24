from django.db import models
from django.core.urlresolvers import reverse
from traceability.models.business import Business


class Customer(Business):
    class Meta:
        app_label = 'traceability'

    def get_absolute_url(self):
        return reverse(
            'traceability:customer:customer_detail',
            args=[self.id], )
