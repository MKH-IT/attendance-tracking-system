# Generated by Django 5.0.6 on 2024-05-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("address", models.TextField()),
                ("phone", models.CharField(max_length=20)),
                (
                    "institution_type",
                    models.CharField(
                        choices=[
                            ("educational_center", "EDUCATIONAL_CENTER"),
                            ("school", "SCHOOL"),
                            ("university", "UNIVERSITY"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
            options={
                "verbose_name": "Organization",
                "verbose_name_plural": "Organizations",
            },
        ),
    ]
