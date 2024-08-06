from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .pdf import html2pdf
from decimal import Decimal


# Create your views here.

def index(request):
    biller = bill.objects.all()
    total_bags = 0
    total_kgs = Decimal('0.0')
    total_amount_rs = Decimal('0.0')

    for item in biller:
        try:
            item.Amount_Rs = Decimal(item.Total_Kgs) * Decimal(item.Rate_Per_Kg)
        except (ValueError, TypeError):
            item.Amount_Rs = Decimal('0.0')
        total_bags += int(item.Bags) if item.Bags else 0
        total_kgs += Decimal(item.Total_Kgs) if item.Total_Kgs else Decimal('0.0')
        total_amount_rs += item.Amount_Rs

    # Fetch the latest inserted value from Deduction
    latest_deduction = deduction.objects.order_by('-id').first()

    if latest_deduction:
        latest_deduction.Cooli_Rent = latest_deduction.Cooli_Rent * total_bags
        latest_deduction.Commission = total_amount_rs * Decimal('0.05')
        latest_deduction.Brokerage = total_amount_rs * Decimal('0.03')
        total_deduction = latest_deduction.Cooli_Rent + latest_deduction.LF_Amount + latest_deduction.Commission + latest_deduction.Brokerage
        total_net_amount = total_amount_rs - total_deduction
    else:
        total_deduction = Decimal('0.0')
        total_net_amount = total_amount_rs

    context = {
        'total_bags': total_bags,
        'total_kgs': total_kgs,
        'total_amount_rs': total_amount_rs,
        'biller': biller,
        'latest_deduction': latest_deduction,
        'total_deduction': total_deduction,
        'total_net_amount': total_net_amount,
    }

    return render(request,"index.html",context)
def add(request):
    return render(request,"add.html")
def addrec(request):
    a=request.POST["LOT_Name"]
    b=request.POST["Bags"]
    c=request.POST["Total_Kgs"]
    d=request.POST["Rate_Per_Kg"]
    biller=bill(LOT_Name=a,Bags=b,Total_Kgs=c,Rate_Per_Kg=d)
    biller.save()
    return redirect("/")
def delete(request,id):
    biller=bill.objects.get(id=id)
    biller.delete()
    return redirect("/")
def update(request,id):
    biller=bill.objects.get(id=id)
    return render(request,"update.html",{"biller":biller})
def uprec(request,id):
    a=request.POST["LOT_Name"]
    b=request.POST["Bags"]
    c=request.POST["Total_Kgs"]
    d=request.POST["Rate_Per_Kg"]
    biller=bill.objects.get(id=id)
    biller.LOT_Name=a
    biller.Bags=b
    biller.Total_Kgs=c
    biller.Rate_Per_Kg=d
    biller.save()
    return redirect("/")
def pdf(request):
    biller = bill.objects.all()
    total_bags = 0
    total_kgs = Decimal('0.0')
    total_amount_rs = Decimal('0.0')

    for item in biller:
        try:
            item.Amount_Rs = Decimal(item.Total_Kgs) * Decimal(item.Rate_Per_Kg)
        except (ValueError, TypeError):
            item.Amount_Rs = Decimal('0.0')
        total_bags += int(item.Bags) if item.Bags else 0
        total_kgs += Decimal(item.Total_Kgs) if item.Total_Kgs else Decimal('0.0')
        total_amount_rs += item.Amount_Rs

    # Fetch the latest inserted value from Deduction
    latest_deduction = deduction.objects.order_by('-id').first()

    if latest_deduction:
        latest_deduction.Cooli_Rent = latest_deduction.Cooli_Rent * total_bags
        latest_deduction.Commission = total_amount_rs * Decimal('0.05')
        latest_deduction.Brokerage = total_amount_rs * Decimal('0.03')
        total_deduction = latest_deduction.Cooli_Rent + latest_deduction.LF_Amount + latest_deduction.Commission + latest_deduction.Brokerage
        total_net_amount = total_amount_rs - total_deduction
    else:
        total_deduction = Decimal('0.0')
        total_net_amount = total_amount_rs

    context = {
        'total_bags': total_bags,
        'total_kgs': total_kgs,
        'total_amount_rs': total_amount_rs,
        'biller': biller,
        'latest_deduction': latest_deduction,
        'total_deduction': total_deduction,
        'total_net_amount': total_net_amount,
    }

    pdf=html2pdf("pdf.html",context)
    return HttpResponse(pdf,content_type="application/pdf")
def ded(request):
    return render(request,"ded.html")
def dedrec(request):
    a=request.POST["Cooli_Rent"]
    b=request.POST["LF_Amount"]
    ded=deduction(Cooli_Rent=a,LF_Amount=b)
    ded.save()
    return redirect("/")
