from django.contrib import admin
from .models import bill,deduction,total
# Register your models here.
class billadmin(admin.ModelAdmin):
    list_display="LOT_Name","Bags","Total_Kgs","Rate_Per_Kg","Amount_Rs"
admin.site.register(bill,billadmin)
class deductionadmin(admin.ModelAdmin):
    list_display="Cooli_Rent","LF_Amount","Brokerage"
admin.site.register(deduction,deductionadmin)
class totaladmin(admin.ModelAdmin):
    list_display="totalBags","totalkgs","totalAmount","Deduction","totalnetAmount"
admin.site.register(total,totaladmin)
