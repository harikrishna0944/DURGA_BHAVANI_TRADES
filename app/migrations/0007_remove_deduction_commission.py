# Generated by Django 4.1.3 on 2024-07-23 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_alter_bill_amount_rs_alter_bill_bags_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="deduction",
            name="Commission",
        ),
    ]
