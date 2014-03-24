from django.contrib import admin
from traceability.models.material import MaterialType, Material


class MaterialAdmin(admin.ModelAdmin):
    search_fields = ['material_id']
    list_display = (
        'material_type',
        'material_id',
        'purchase_date',
        'expiration_date', )


class MaterialTypeAdmin(admin.ModelAdmin):
    list_display = ('material_type', )
