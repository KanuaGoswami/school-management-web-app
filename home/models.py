from django.db import models
from django.contrib.auth.models import User
import datetime



# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    class Meta:
        unique_together = ['name','email','subject','message']
    def __str__(self):
        return self.name

# class Student(models.Model):
#     rollno = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)
#     dob = models.CharField(max_length=200)
#     clas = models.CharField(max_length=200)
#     fname = models.CharField(max_length=200)
#     mname = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     mobile = models.CharField(max_length=200)
#     gender= models.CharField(max_length=255)
#     email = models.CharField(max_length=255)


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    dob = models.CharField(max_length=10)
    designation = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'image')
    desc = models.TextField()
    gender = models.CharField(max_length=20)
    qualification = models.CharField(max_length=30)
    class Meta:
        unique_together=['name','address','mobile','dob','designation','desc','gender','qualification']
    

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=200)
    image = models.ImageField(upload_to = 'img')
    class Meta:
        unique_together = ["title","desc"]
    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=200)
    def __str__(self):
        return self.email



class Student(models.Model):
    # id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    rollno = models.CharField(max_length=255,default='null')
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)
    mobileno = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img',default='')
    cl = models.CharField(max_length=200,default='')
    class Meta:
        unique_together = ["name", "rollno","fname","mname","mobileno","dob","gender","address","postcode","cl"]
    

class Transaction(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    amount = models.CharField(max_length=200)
    class Meta:
        unique_together = ["student", "amount"]
    
     
class Result(models.Model):
    id=models.AutoField(primary_key=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    examname = models.CharField(max_length=249,default='')
    english = models.IntegerField(default=0)
    math = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    sst = models.IntegerField(default=0)
    hindi = models.IntegerField(default=0)
    class Meta:
        unique_together = ['student','examname','english','math','science','sst','hindi']

