from django.shortcuts import render
from .models import book_table,pen_table,signup_table
from .forms import Regform

# Create your views here.
def index(req):
    return render(req,"index.html")



def signup(request):
    if request.method == 'POST':
      fname= request.POST.get('nm')
      mob= request.POST.get('mob')
      mail= request.POST.get('mail')
      password= request.POST.get('pass')
      cpassword= request.POST.get('cpass')
      obj= signup_table.objects.create(name=fname,mobile=mob,email=mail,pswd=password,cpswd=cpassword)
      obj.save()
      if obj:
          msg ="New user added.."
          return render(request,"index.html",{"success":msg})
      return render(request,"signup.html")
        # return render(request,'login.html')
        # return redirect("/log")
    else:
        return render(request,'signup.html')
    # return render(request,'signup.html')    



def login(request):
  if request.method =='POST':
    email=request.POST.get('name')
    pas=request.POST.get('pas')
    obj= signup_table.objects.filter(email=email, pswd=pas)
    if obj:
      request.session['ema']=email
      request.session['psa']=pas
      for m in obj:
        idl = m.id
      request.session['idn']=idl
      return render(request,'home.html')  
    else:
      msg = 'Invalid Credentials'
      return render(request,'login.html',{"error":msg}) 
  return render(request,'login.html')    
 

# def changepass(request):
#     return render(request,'changepassword.html')  

# def users(request):
#   obb=Reg_tbl.objects.all()
#   return render(request,'users.html',{"data":obb})  

# def edit(request,pk):
#   ob=Reg_tbl.objects.filter(id=pk)
#   if request.method=='POST':
#     fnm=request.POST.get('fn')
#     idl=request.POST.get('idn')
#     email=request.POST.get('em')
#     mob=request.POST.get('mb')
#     pas=request.POST.get('ps')
#     obc=Reg_tbl.objects.filter(id=idl)
#     obc.update(fnm=fnm, mob=mob, eml=email, psw=pas)
#     return redirect("/users")

#   return render(request,"oneuser.html",{"data":ob})        

# def delete(request,pk):
#   obt=Reg_tbl.objects.filter(id=pk)
#   obt.delete()
#   return redirect("/users")
  









def books(req):
    return  render(req,"books.html")
def addbook(req):
    if req.method=='POST':
        bn=req.POST.get('bn')
        au=req.POST.get('au')
        au=str(au)
        au=au.lower()
        pr=req.POST.get('pr')
        ds=req.POST.get('desc')
        obj=book_table.objects.create(bname=bn,author=au,price=pr,desc=ds)
        obj.save()
        if obj:
            msg ="New book added.."
            return render(req,"addbook.html",{"success":msg})
    return render(req,"addbook.html")

def viewbooks(req):
    ob=book_table.objects.all()
    return render(req,'books.html',{"books":ob})

def searchbooks(req):
    if req.method=='POST':
        au = req.POST.get('au')
        au = au.lower()
        obj2 = book_table.objects.filter(author=au)
        return render(req,"booksearch.html",{"books2":obj2})
    return render(req,"booksearch.html")

def addpen(req):
    if req.method=='POST':
        pnm=req.POST.get('nm')
        pimg=req.FILES.get('pic')
        prc=req.POST.get('pr')
        obj= pen_table.objects.create(pname=pnm,img=pimg,price=prc)
        obj.save()
        if obj:
            return render(req,'addpen.html',{"msg":"details uploaded..."})
    return render(req,'addpen.html')


def viewpens(req):
    ob=pen_table.objects.all()
    return render(req,"viewpens.html",{"pens":ob})

def addcart(req,pk):
    ob=pen_table.objects.filter(id=pk)
    return render(req,"viewpens.html")

def viewform(request):
    form=Regform()
    if request.method=='POST':
        form=Regform(request.POST)
        if form.is_valid():
            fn=form.cleaned_data.get('name')
            mb=form.cleaned_data['mobile']
            obj=signup_table.objects.create(name=fn,mobile=mb)
            obj.save()
            if obj:
                msg="Registration Successfuill"
                return render(request,'formview.html',{"form":form,"success":msg})
    return render(request,"formview.html",{"form":form}) 
 
 
 