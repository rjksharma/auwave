# Generated by Django 4.2.2 on 2023-06-16 16:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0010_auwavedetails_discription_auwavedetails_email"),
    ]

    operations = [
        migrations.RenameField(
            model_name="auwavedetails",
            old_name="Discription",
            new_name="discription",
        ),
    ]