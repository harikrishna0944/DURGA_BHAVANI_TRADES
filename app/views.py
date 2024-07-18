from django.shortcuts import render,redirect,HttpResponse
from .models import bill,deduction,total
from .pdf import html2pdf

# Create your views here.

def index(request):
    biller=bill.objects.all()
    dedc=deduction.objects.all()
    return render(request,"index.html",{"biller":biller,"dedc":dedc})
def add(request):
    return render(request,"add.html")
def addrec(request):
    a=request.POST["LOT_Name"]
    b=request.POST["Bags"]
    c=request.POST["Total_Kgs"]
    d=request.POST["Rate_Per_Kg"]
    e=request.POST["Amount_Rs"]
    biller=bill(LOT_Name=a,Bags=b,Total_Kgs=c,Rate_Per_Kg=d,Amount_Rs=e)
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
    e=request.POST["Amount_Rs"]
    biller=bill.objects.get(id=id)
    biller.LOT_Name=a
    biller.Bags=b
    biller.Total_Kgs=c
    biller.Rate_Per_Kg=d
    biller.Amount_Rs=e
    biller.save()
    return redirect("/")
def pdf(request):
    biller=bill.objects.all()
    dedc=deduction.objects.all()
    totc=total.objects.all()
    pdf=html2pdf("pdf.html",{"biller":biller,"dedc":dedc,"totc":totc})
    return HttpResponse(pdf,content_type="application/pdf")
def ded(request):
    return render(request,"ded.html")
def dedrec(request):
    a=request.POST["Cooli_Rent"]
    b=request.POST["LF_Amount"]
    c=request.POST["Commission"]
    d=request.POST["Brokerage"]
    ded=deduction(Cooli_Rent=a,LF_Amount=b,Commission=c,Brokerage=d)
    ded.save()
    return redirect("/")
def totalrec(request):
    if request.method == 'POST':
        a = request.POST.get('TotalBags', '0')
        b = request.POST.get('totalkgs', '0')
        c = request.POST.get('totalAmount', '0.00')
        d = request.POST.get('Deduction', '0.00')
        e= request.POST.get('totalnetAmount', '0.00')
        totr=total(totalBags=a,totalkgs=b, totalAmount=c, Deduction=d,totalnetAmount=e)
        totr.save()
        return redirect("/")
    
def deleteded(request,id):
    dedc=deduction.objects.get(id=id)
    dedc.delete()
    return redirect("/")
    

