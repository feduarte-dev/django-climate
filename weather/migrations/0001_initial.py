# Generated by Django 4.2.3 on 2024-04-30 20:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=60)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
        ),
    ]