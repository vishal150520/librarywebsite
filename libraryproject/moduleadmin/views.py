from MySQLdb import Connection
from django.db import connection
from django.shortcuts import redirect, render

# Create your views here.
import re
from django.http import Http404, HttpResponse
from django.shortcuts import render
from matplotlib import category
from urllib3 import Retry

from moduleadmin.models import admindetails,bookdetails,studentdetails
# Create your views here.
# this view for home page return
def home(request):
    return render(request,'home.html')
    
# this view for admin sign up form
def adminsignup1(request):
    return render(request,'adminsignup.html')

# this view for student login
def studentlogin1(request):
    return HttpResponse("student login")

# this view for student sign up
def studentsignup1(request):
    return render(request,'stusign.html')

# this view for  admin signup
def adminsignup11(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        dateofbirth=request.POST.get('dateofbirth')
        email=request.POST.get('email')
        contactno=request.POST.get('contactno')
        password=request.POST.get('password')
        o=admindetails(firstName=fname,lastName=lname,gender=gender,dateofbirth=dateofbirth,email=email,contactno=contactno,password=password)
        o.save()
    n="sucessfully signup"
    return render(request,'home.html',{'n':n})

# this view for admin login form
def adlog11(request):
    return render(request,'adminlogin.html')

# this view for admin  log in
def admins12(request):
      if request.method=='POST':
        user=request.POST.get('user')
        pass1=request.POST.get('pass')
        cur=connection.cursor()
        h="select 1 from moduleadmin_admindetails where email='"+user+"' AND password='"+pass1+"';"
        cur.execute(h)
        if not cur.fetchmany():
            return HttpResponse('not')
        else:
            n="Sucessfully Login '"+user+"'"
      return render(request,'adminfunction.html',{'n':n})

# this view for admin log out
def alogout1(request):
    return render(request,'home.html')

# this view for add book form
def addb1(request):
    return render(request,'adbook.html')

# this view for save book details
def saveb1(request):
    if request.method=='POST':
        bname=request.POST.get('bname')
        wname=request.POST.get('wn')
        edition=request.POST.get('edition')
        price=request.POST.get('price')
        cat=request.POST.get('cate')
        pub=request.POST.get('pub')
        o=bookdetails(bookName=bname,writerName=wname,edition=edition,price=price,catogory=cat,publisher=pub)
        o.save()    
    n="sucessfully add book"
    return render(request,'adminfunction.html',{'n':n})

# this view for update book details form
def updatebook12(request):
    return render(request,'updatebook.html')

# this view for update book details
def updatebook14(request):
    if request.method=='POST':
        id1=request.POST.get('id')
        bname=request.POST.get('bname')
        wname=request.POST.get('wn')
        edition=request.POST.get('edition')
        price=request.POST.get('price')
        cate=request.POST.get('cate')
        pub=request.POST.get('pub')
        o=bookdetails.objects.get(bookName=bname)
        o.bookName=bname
        o.writerName=wname
        o.edition=edition
        o.price=price
        o.catogory=cate
        o.publisher=pub
        o.save()
    n="data update"
    return render(request,'adminfunction.html',{'n':n})

# this view for delete book form
def delb1(request):
    return render(request,"del.html")

# this view for delete book
def delb2(request):
    if request.method=='POST':
        bookname=request.POST.get('bname')
        o=bookdetails.objects.get(bookName=bookname)
        o.delete()
        n="delete book"
        return render(request,'adminfunction.html',{'n':n})
    else:
        n="invalid name"
        return render(request,'del.html',{'n':n})

# this view for show all details of books
def getallbooks1(request):
    data=bookdetails.objects.all()
    return render(request,'booklist.html',{'data':data})

# this view for back menu 
def back(request):
    return render(request,'home.html')

# this view for logout
def logout2(request):
    return render(request,'home.html')

# this view for student signup
def stusign1(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        dob=request.POST.get('dateofbirth')
        course=request.POST.get('course')
        rollno=request.POST.get('rollno')
        dept=request.POST.get('dept')
        o=studentdetails(studentfname=fname,studentlname=lname,gender=gender,dob=dob,course=course,rollno=rollno,department=dept)
        o.save()    
    n="sucessfully signup"
    return render(request,'home.html',{'n':n})

# this view for student login form
def studentlogin1(request):
    return render(request,'studentlogin.html')

# this view for student login
def stulog1(request):
    if request.method=='POST':
        user=request.POST.get('rollno')
        pass1=request.POST.get('dob')
        cur=connection.cursor()
        h="select 1 from moduleadmin_studentdetails where rollno='"+user+"' AND dob='"+pass1+"';"
        cur.execute(h)
        if not cur.fetchmany():
            return HttpResponse('not')
        else:
            n="Sucessfully Login '"+user+"'"
        return render(request,'studenthome.html',{'n':n})

# this view for student all details
def viewall1(request):
    data=bookdetails.objects.all()
    return render(request,'booklist.html',{'data':data})

# this view for student log out
def stulogout1(request):
    return render(request,'home.html')