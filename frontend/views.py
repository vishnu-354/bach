from django.shortcuts import render, redirect

from backend.models import instrumentdb, productdb
from frontend.models import customerdb, reviewdb, deliverydb

from django.contrib import messages


# Create your views here.
def home(req):
    data=instrumentdb.objects.all()
    return render(req, "home.html", {'data': data})

def contact(req):
    data = instrumentdb.objects.all()
    return render(req, "contact.html",{'data': data})

def inst(req,itemcatg):
    data = instrumentdb.objects.all()
    print("item",itemcatg)
    catg=itemcatg.upper()
    products=productdb.objects.filter(instrument= itemcatg)
    context={
        'products': products,
        'catg' : catg,
        'data': data
    }
    return render(req, "instrument.html",context)

def single(req,dataid):
    datas= instrumentdb.objects.all()
    da= productdb.objects.all()
    data= productdb.objects.get(id=dataid)
    return render(req, "single.html",{'data':data, 'da':da, "datas": datas})

def loginc(req):
    data = instrumentdb.objects.all()
    return render(req, "loginc.html", {'data': data})

def deal(req):
    data= instrumentdb.objects.all()
    da = productdb.objects.all()
    return render(req, "deal.html",{ 'da':da, 'data': data})

def customer(req):
    if req.method == "POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        pa=req.POST.get('password')
        cp=req.POST.get('cpassword')
        if pa==cp:
            obj=customerdb(name=na, email=em, password=pa, cpassword=cp)
            obj.save()
            messages.success(req,"REGISTERED SUCCESSFULLY")
            return redirect(loginc)
        else:
            messages.warning(req,"Password  MISSMATCH")
            return render(req, "loginc.html")

def customerl(req):
    if req.method=="POST":
        na=req.POST.get('name')
        word=req.POST.get('password')
        if customerdb.objects.filter(name=na, password=word).exists():
            req.session['name']=na
            req.session['password']=word
            messages.success(req, "WELCOME ")
            return redirect(home)
        else:
            messages.error(req, "RETRY")
            return render(req, "loginc.html", {'msg': "SORRY.....RETRY"})

def customerd(req):
    del req.session['name']
    del req.session['password']
    messages.warning(req, "LOGGED OUT")
    return redirect(home)

def reviewc(req):
    if req.method=="POST":
        na=req.POST.get('Name')
        em=req.POST.get('Email')
        me=req.POST.get('Message')
        obj=reviewdb(Name=na, Email=em, Message=me)
        obj.save()
        return render(req, "contact.html")

def delivery(req, dataid):
    if req.method=="POST":
        pr = req.POST.get('Products')
        na = req.POST.get('Name')
        em = req.POST.get('Email')
        ph = req.POST.get('Ph_no')
        ad = req.POST.get('Address')
        qt = req.POST.get('qty')
        to = req.POST.get('totalprice')
        productdb.objects.get(id=dataid)
        obj=deliverydb(Products=pr ,Name=na, Email=em, Ph_no=ph, Address=ad, qty=qt, totalprice=to)
        obj.save()
        messages.success(req, "ordered successfully")
        return redirect(home)
