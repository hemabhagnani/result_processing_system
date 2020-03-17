from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    dept_no_list = department.objects.all().order_by('dept_no')
    scheme_no_list=scheme.objects.all().order_by('scheme_no')
    sub_no_list=subjects.objects.all().order_by('sub_no')
    context = {
    'scheme_no_list': scheme_no_list,
    'dept_no_list': dept_no_list,
    'sub_no_list' : sub_no_list

 }
    return render(request,'job/home.html', context)

def dept_form(request):
    if request.method=='POST':
        Department=department()
        Department.dept_name=request.POST['dept_name']
        Department.dept_no=request.POST['dept_no']
        Department.save()
        return redirect('home')

    else:
       return render(request,'job/home.html')

def student_form(request):
    if request.method=='POST':
        Student=student()
        Student.fname=request.POST['fname']
        Student.lname=request.POST['lname']
        Student.enroll_no=request.POST['enroll_no']
        student_dept_no=request.POST['student_dept_no']
        Student.student_dept_no=department.objects.get(dept_no=student_dept_no)
        Student.save()
        return redirect('home')

    else:
       return render(request,'job/home.html')

def scheme_form(request):
    if request.method=='POST':
        Scheme=scheme()
        Scheme.scheme_no=request.POST['scheme_no']
        Scheme.theory_cr=request.POST['theory_cr']
        Scheme.practical_cr=request.POST['practical_cr']
        Scheme.max_th=request.POST['max_th']
        Scheme.max_mid=request.POST['max_mid']
        Scheme.max_pr=request.POST['max_pr']
        Scheme.save()
        return redirect('home')

    else:
       return render(request,'job/home.html')


def sub_form(request):
    if request.method=='POST':
        Subject=subjects()
        Subject.sub_no=request.POST['sub_no']
        Subject.sub_name=request.POST['sub_name']
        sub_dept_no=request.POST['sub_dept_no']
        Subject.sub_dept_no=department.objects.get(dept_no=sub_dept_no)
        sub_scheme_no=request.POST['sub_scheme_no']
        Subject.sub_scheme_no=scheme.objects.get(scheme_no=sub_scheme_no)
        Subject.Sem=request.POST['Sem']
        Subject.save()
        return redirect('home')

    else:
       return render(request,'job/home.html')

def marks_form(request):
    if request.method=='POST':
        Marks=marks()
        marks_sub_no=request.POST['marks_sub_no']
        Marks.marks_sub_no=subjects.objects.get(sub_no=marks_sub_no)
        marks_enroll_no=request.POST['marks_enroll_no']
        Marks.marks_enroll_no=student.objects.get(enroll_no=marks_enroll_no)
        Marks.th=request.POST['th']
        Marks.pr=request.POST['pr']
        Marks.mid=request.POST['mid']
        Marks.save()
        return redirect('home')

    else:
       return render(request,'job/home.html')
