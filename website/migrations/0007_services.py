# Generated by Django 4.2.2 on 2023-06-15 10:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0006_alter_ourteams_images"),
    ]

    operations = [
        migrations.CreateModel(
            name="Services",
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
                ("icon", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("discription", models.CharField(max_length=255)),
            ],
        ),
    ]