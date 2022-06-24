from django.db import models
from django.forms import CharField

# Create your models here.
class admindetails(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dateofbirth=models.EmailField(unique=True,max_length=50)
    email=models.CharField(max_length=50)
    contactno=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
class bookdetails(models.Model):
    bookName=models.CharField(max_length=50)
    writerName=models.CharField(max_length=50)
    edition=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    catogory=models.CharField(max_length=50)
    publisher=models.CharField(max_length=50)
class studentdetails(models.Model):
    studentfname=models.CharField(max_length=50)
    studentlname=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    rollno=models.CharField(max_length=50)
    department=models.CharField(max_length=50)