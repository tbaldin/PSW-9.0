# Generated by Django 4.2.9 on 2024-01-21 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("apostilas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ViewApostila",
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
                ("ip", models.GenericIPAddressField()),
                (
                    "apostila",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="apostilas.apostila",
                    ),
                ),
            ],
        ),
    ]
