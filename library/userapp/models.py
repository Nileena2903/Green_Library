from django.db import models

# Create your models here.

class signup_table(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    pswd=models.CharField(max_length=50)
    cpswd=models.CharField(max_length=50)
    

class book_table(models.Model):
    bname=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.IntegerField()
    desc=models.CharField(max_length=100)

class pen_table(models.Model):
    pname=models.CharField(max_length=50)
    img=models.FileField(upload_to='penpics')
    price=models.IntegerField()
    