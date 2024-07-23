from django.db import models

# Create your models here.
class bill(models.Model):
    LOT_Name=models.CharField(max_length=100)
    Bags=models.IntegerField()
    Total_Kgs=models.DecimalField(max_digits=10, decimal_places=2)
    Rate_Per_Kg=models.DecimalField(max_digits=10, decimal_places=2)
    Amount_Rs=models.DecimalField(max_digits=15, decimal_places=2)

class deduction(models.Model):
    Cooli_Rent=models.DecimalField(max_digits=10, decimal_places=2)
    LF_Amount=models.DecimalField(max_digits=10, decimal_places=2)
    Brokerage=models.DecimalField(max_digits=10, decimal_places=2)

class total(models.Model):
    totalBags = models.IntegerField()
    totalkgs = models.IntegerField()
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    Deduction = models.DecimalField(max_digits=10, decimal_places=2)
    totalnetAmount = models.DecimalField(max_digits=10, decimal_places=2)
    

