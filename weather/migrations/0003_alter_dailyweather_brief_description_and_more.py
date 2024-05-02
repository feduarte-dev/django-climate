# Generated by Django 4.2.3 on 2024-05-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("weather", "0002_dailyweather"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyweather",
            name="brief_description",
            field=models.CharField(
                choices=[
                    ("Ensolarado", "Ensolarado"),
                    ("Nublado", "Nublado"),
                    ("Chuvoso", "Chuvoso"),
                    ("Parcialmente nublado", "Parcialmente nublado"),
                    ("Neve", "Neve"),
                    ("Granizo", "Granizo"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="dailyweather",
            name="date",
            field=models.DateField(),
        ),
    ]