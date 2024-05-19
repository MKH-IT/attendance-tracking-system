from django.db import models

from common.enums import InstitutionType


class Organizations(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    institution_type = models.CharField(
        max_length=20,
        choices=[(tag.value, tag.name) for tag in InstitutionType],
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} - {self.institution_type}"

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
