from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from backend.models import admindb, instrumentdb, productdb
from frontend.models import deliverydb



from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

from frontend.models import reviewdb


# Create your views here.
def index(req):
    da= deliverydb.objects.all()
    data = productdb.objects.all()
    d=deliverydb.objects.all().count()
    i=instrumentdb.objects.all().count()
    p=productdb.objects.all().count()
    r=reviewdb.objects.all().count()
    return render(req, "index.html", {'data': data, 'da':da, 'd':d ,'i':i, 'p':p ,'r':r})

def done(req, dataid):
    data = deliverydb.objects.get(id=dataid)
    data.delete()
    return redirect(index)

def addadmin(req):
    return render(req, "pageone.html")

def register(req):
    if req.method == "POST":
        na= req.POST.get('Name')
        em= req.POST.get('Email')
        mo= req.POST.get('Mobileno')
        pa= req.POST.get('Password')
        im= req.FILES['image']
        obj= admindb(Name=na, Email=em, Mobileno=mo, Password=pa, image=im)
        obj.save()
        return redirect(addadmin)

def displaya(req):
    data = admindb.objects.all()
    return render(req, "pagetwo.html",{'data':data})

def editadmin(req,dataid):
    data= admindb.objects.get(id=dataid)
    return render(req, "pagethree.html", {'data': data})

def updateadmin(req,dataid):
    if req.method=="POST":
        na= req.POST.get('Name')
        em= req.POST.get('Email')
        mo= req.POST.get('Mobileno')
        pa= req.POST.get('Password')
        try:
            img=req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).image
        admindb.objects.filter(id=dataid).update(Name=na, Email=em, Mobileno=mo, Password=pa, image=file)
        return redirect(displaya)


def deleteadmin(req,dataid):
    data= admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaya)

def instrumentone(req):
    return render(req, "instrumentone.html")

def addinstrument(req):
    if req.method =="POST":
        ns =req.POST.get('instrument')
        img = req.FILES['image']
        obj=instrumentdb(instrument=ns, image=img)
        obj.save()
        return redirect(instrumentone)

def instrumenttwo(req):
    data = instrumentdb.objects.all()
    return render(req, "instrumenttwo.html", {'data': data})


def editinst(req,dataid):
    data = instrumentdb.objects.get(id=dataid)
    return render(req, "instrumentthree.html", {'data':data})

def updateinst(req,dataid):
    if req.method =="POST":
        ns =req.POST.get('instrument')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = instrumentdb.objects.get(id=dataid).image
        instrumentdb.objects.filter(id=dataid).update(instrument=ns, image=file)
        return redirect(instrumenttwo)

def deleteinst(req, dataid):
    data= instrumentdb.objects.filter(id=dataid)
    data.delete()
    return redirect(instrumenttwo)


def productone(req):
    data= instrumentdb.objects.all()
    return render(req, "productone.html", {'data': data})

def addproduct(req):
    if req.method=="POST":
         ns = req.POST.get('instrument')
         pr = req.POST.get('Product')
         qu = req.POST.get('Quantity')
         ri = req.POST.get('Price')
         de = req.POST.get('Description')
         im = req.FILES['image']
         obj=productdb(instrument=ns, Product=pr, Quantity=qu, Price=ri, Description=de, image=im)
         obj.save()
         return redirect(productone)

def producttwo(req):
    data = productdb.objects.all()
    return render(req, "producttwo.html", {'data': data})

def editproduct(req, dataid):
    da = productdb.objects.all()
    data = productdb.objects.get(id=dataid)
    print(da)
    return render(req, "productthree.html", {'data':data, 'da': da})

def updateproduct(req, dataid):
    if req.method=="POST":
        ns = req.POST.get('instrument')
        pr = req.POST.get('Product')
        qu = req.POST.get('Quantity')
        ri = req.POST.get('Price')
        de = req.POST.get('Description')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).image
        productdb.objects.filter(id=dataid).update(instrument=ns, Product=pr, Quantity=qu, Price=ri, Description=de, image=file)
        return redirect(producttwo)

def deleteproduct(req, dataid):
    data = productdb.objects.get(id=dataid)
    data.delete()
    return redirect(producttwo)


def logina(req):
    return render(req, "login.html")

def mainlogin(req):
    if req.method=="POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(req, user)
                req.session['username']=username_r
                req.session['password']=password_r
                return redirect(index)
            else:
                return redirect(logina)
        else:
            return redirect(logina)


def adminlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(logina)


def reviewmess(req):
    data = reviewdb.objects.all()
    return render(req, "review.html", {'data':data})

def reviewdelete(req,dataid):
    data=reviewdb.objects.get(id=dataid)
    data.delete()
    return redirect(reviewmess)