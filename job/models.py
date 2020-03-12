from django.db import models

# Create your models here.
class department(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dept_name=models.TextField(max_length=50)

class student(models.Model):
    enroll_no=models.TextField(primary_key=True,max_length=20)
    dept_no=models.ForeignKey(department,on_delete=models.CASCADE)
    fname=models.TextField(max_length=50)
    lname=models.TextField(max_length=50)

class scheme(models.Model):
    scheme_no=models.IntegerField(primary_key=True)
    theory_cr=models.IntegerField(max_length=5)
    practical_cr=models.IntegerField(max_length=5)
    max_th=models.IntegerField(max_length=5)
    max_pr=models.IntegerField(max_length=5)
    max_mid=models.IntegerField(max_length=5)

class subjects(models.Model):
    sub_no=models.IntegerField(primary_key=True)
    dept_no=models.ForeignKey(department,on_delete=models.CASCADE)
    scheme_no=models.ForeignKey(scheme,on_delete=models.CASCADE)



class marks(models.Model):
    enroll_no=models.ForeignKey(student,on_delete=models.CASCADE)
    sub_no=models.ForeignKey(subjects,on_delete=models.CASCADE)
    th=models.IntegerField(max_length=5)
    pr=models.IntegerField(max_length=5)
    mid=models.IntegerField(max_length=5)

class backlog(models.Model):
    enroll_no=models.ForeignKey(student,on_delete=models.CASCADE)
    sub_no=models.ForeignKey(subjects,on_delete=models.PROTECT)

class result(models.Model):
    enroll_no=models.ForeignKey(student,on_delete=models.CASCADE)
    sem1=models.FloatField(default='0',max_length=5)
    sem2=models.FloatField(default='0',max_length=5)
    sem3=models.FloatField(default='0',max_length=5)
    sem4=models.FloatField(default='0',max_length=5)
    sem5=models.FloatField(default='0',max_length=5)
    sem6=models.FloatField(default='0',max_length=5)
    sem7=models.FloatField(default='0',max_length=5)
    sem8=models.FloatField(default='0',max_length=5)
    ogpa=models.FloatField(default='0',max_length=5)
