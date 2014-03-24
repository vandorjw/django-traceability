from django.contrib import admin
from traceability.models.shipment import Shipment


class ShipmentAdmin(admin.ModelAdmin):
    search_fields = ['invoice_number', 'customer']
    list_display = ('date_shipped', 'customer', 'address', 'invoice_number')


admin.site.register(Shipment, ShipmentAdmin)
