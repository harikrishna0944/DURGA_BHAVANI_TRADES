from django.contrib import admin
from .models import *
# Register your models here.
class billadmin(admin.ModelAdmin):
    list_display="LOT_Name","Bags","Total_Kgs","Rate_Per_Kg"
admin.site.register(bill,billadmin)
class deductionadmin(admin.ModelAdmin):
    list_display="Cooli_Rent","LF_Amount"
admin.site.register(deduction,deductionadmin)
