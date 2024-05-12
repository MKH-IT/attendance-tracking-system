from django.contrib import admin

from organization.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone", "institution_type")
    search_fields = ("name", "address", "phone", "institution_type")
    list_filter = ("institution_type",)
