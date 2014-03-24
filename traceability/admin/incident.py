from django.contrib import admin
from traceability.models.incident import Incident, Update


class UpdateInline(admin.TabularInline):
    model = Update
    extra = 1


class IncidentAdmin(admin.ModelAdmin):
    inlines = [
        UpdateInline,
    ]
    list_display = (
        'date_time',
        'title',
        'severity_level',
        'is_resolved', )

admin.site.register(Incident, IncidentAdmin)
