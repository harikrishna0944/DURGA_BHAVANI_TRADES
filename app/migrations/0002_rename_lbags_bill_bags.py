# Generated by Django 4.1.3 on 2024-07-01 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bill",
            old_name="lBags",
            new_name="Bags",
        ),
    ]