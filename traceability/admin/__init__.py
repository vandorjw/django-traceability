"""Admin models for Traceability"""
from django.contrib import admin

from traceability.models.location import *
from traceability.models.employee import *
from traceability.models.customer import *
from traceability.models.supplier import *
from traceability.models.incident import *
from traceability.models.material import *
from traceability.models.batch import *
from traceability.models.item import *
from traceability.models.shipment import *
from traceability.admin.employee import *
from traceability.admin.incident import *
from traceability.admin.material import *
from traceability.admin.batch import *
from traceability.admin.item import *
from traceability.admin.shipment import *

admin.site.register(Country)
admin.site.register(AdminArea)
admin.site.register(Locality)
admin.site.register(Address)
admin.site.register(Item, ItemAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(MaterialType, MaterialTypeAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Customer)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Incident, IncidentAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Supplier)

