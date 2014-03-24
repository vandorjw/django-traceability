from django.contrib import admin
from traceability.models.material import MaterialName, Material


class MaterialAdmin(admin.ModelAdmin):
    search_fields = ['material_id']
    list_display = (
        'material_type',
        'material_id',
        'purchase_date',
        'expiration_date', )


class MaterialNameAdmin(admin.ModelAdmin):
    list_display = ('material_type', )


admin.site.register(MaterialName, MaterialNameAdmin)
admin.site.register(Material, MaterialAdmin)
