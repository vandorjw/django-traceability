from django.db import models
from django.core.urlresolvers import reverse
from traceability.models.business import Business


class Supplier(Business):
	
    class meta:
        app_label = 'traceability'

    def get_absolute_url(self):
        return reverse(
            'traceability:supplier:supplier_detail',
            args=[self.id], )
