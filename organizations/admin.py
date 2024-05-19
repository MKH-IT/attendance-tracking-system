from django.contrib import admin

from organizations.models import Organizations


@admin.register(Organizations)
class OrganizationsAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone", "institution_type")
    search_fields = ("name", "address", "phone", "institution_type")
    list_filter = ("institution_type",)
