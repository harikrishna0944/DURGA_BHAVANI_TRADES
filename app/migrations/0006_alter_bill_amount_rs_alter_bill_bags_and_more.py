# Generated by Django 4.1.3 on 2024-07-08 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_total_deduction_alter_total_totalamount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bill",
            name="Amount_Rs",
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name="bill",
            name="Bags",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="bill",
            name="Rate_Per_Kg",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="bill",
            name="Total_Kgs",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="deduction",
            name="Brokerage",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="deduction",
            name="Commission",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="deduction",
            name="Cooli_Rent",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="deduction",
            name="LF_Amount",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="total",
            name="Deduction",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="total",
            name="totalAmount",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="total",
            name="totalBags",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="total",
            name="totalkgs",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="total",
            name="totalnetAmount",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]