from datetime import datetime, timedelta
from django.db import models


class InventoryManager(models.Manager):
    def get_queryset(self):
        return super(InventoryManager, self).get_queryset().filter(
            shipment__isnull=True, ).distinct()

    def days_0_30(self):
        # Example method
        start_date = datetime.now() + timedelta(-30)
        return super(InventoryManager, self).get_queryset().filter(
            shipment__isnull=True,
            batch__creation_date__gte = start_date, )

