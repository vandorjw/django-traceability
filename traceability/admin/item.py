from django.contrib import admin
from traceability.models.Item import Item


class ItemAdmin(admin.ModelAdmin):
    search_fields = ['item_id']
    list_display = ('item_id',
                    'batch',
                    'item_age',
                    'weight', )

admin.site.register(Item, ItemAdmin)

