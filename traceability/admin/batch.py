from django.contrib import admin
from traceability.models.batch import Batch, Ingredient
from traceability.models.item import Item


class ItemInline(admin.TabularInline):
    model = Item


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1


class BatchAdmin(admin.ModelAdmin):
    inlines = [
        IngredientInline,
        ItemInline,
    ]
    search_fields = ['batch_number']
    list_display = (
        'batch_number',
        'creation_date', )


admin.site.register(Batch, BatchAdmin)
