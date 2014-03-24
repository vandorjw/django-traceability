from django.contrib import admin
from traceability.models.batch import Batch, Input
from traceability.models.item import Item


class ItemInline(admin.TabularInline):
    model = Item


class InputInline(admin.TabularInline):
    model = Input
    extra = 1


class BatchAdmin(admin.ModelAdmin):
    inlines = [
        InputInline,
        ItemInline,
    ]
    search_fields = ['batch_id']
    list_display = (
        'batch_id',
        'creation_date', )
