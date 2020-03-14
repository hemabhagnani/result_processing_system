from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'job/home.html')

def dept_form(request):
    if request.method=='POST':
        Department=department()
        Department.dept_name=request.POST['dept_name']
        Department.dept_no=request.POST['dept_no']
        Department.save()
        return redirect('dept_form')

    else:
       return render(request,'job/home.html')

def student_form(request):
    if request.method=='POST':
        Student=student()
        Student.enroll_no=request.POST['enroll_no']
        Student.fname=request.POST['fname']
        Student.lname=request.POST['lname']
        Student.dept_no=request.POST['dept_no']

        Student.save()
        return redirect('')

    else:
       return render(request,'job/home.html')
