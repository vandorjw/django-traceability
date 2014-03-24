from django.contrib import admin
from traceability.models.location import Country, AdminArea, Locality, Address


admin.site.register(Country)
admin.site.register(AdminArea)
admin.site.register(Locality)
admin.site.register(Address)
