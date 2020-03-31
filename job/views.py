from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request,error_message=''):
    dept_no_list = department.objects.all().order_by('dept_no')
    scheme_no_list=scheme.objects.all()
    sub_no_list=subjects.objects.all().order_by('sub_no')

    context = {
    'scheme_no_list': scheme_no_list,
    'dept_no_list': dept_no_list,
    'sub_no_list' : sub_no_list,
    'error_message':error_message,


 }
    return render(request,'job/home.html', context)

def dept_form(request):
    if request.method=='POST':
        if department.objects.filter(dept_no=request.POST['dept_no']).exists():
            return redirect(home,error_message="Department Already Exist!!")
        Department=department()
        Department.dept_name=request.POST['dept_name']
        Department.dept_no=request.POST['dept_no']
        Department.save()
        return redirect('home')

    else:
       return redirect('home')

def student_form(request):
    if request.method=='POST':
        if student.objects.filter(enroll_no=request.POST['enroll_no']).exists():
            return redirect(home,error_message="Student Already Exist!!")

        Student=student()
        Student.fname=request.POST['fname']
        Student.lname=request.POST['lname']
        Student.enroll_no=request.POST['enroll_no']
        student_dept_no=request.POST['student_dept_no']
        Student.student_dept_no=department.objects.get(dept_no=student_dept_no)
        Student.student_scheme_year=request.POST['student_scheme_year']
        Student.save()
        return redirect('home')

    else:
       return redirect('home')

def scheme_form(request):

        if request.method=='POST':
            if  scheme.objects.filter(scheme_no=request.POST['scheme_no']).exists():
                return redirect(home,error_message="Scheme Already Exist!!")

            sc_no=request.POST['scheme_no']
            th_cr=request.POST['theory_cr']
            pr_cr=request.POST['practical_cr']

            if th_cr=='0':
                Scheme= scheme.objects.create(scheme_no=sc_no, theory_cr=th_cr,practical_cr=pr_cr,max_th='0',max_mid='20',max_pr='80')

            elif pr_cr=='0':
                Scheme= scheme.objects.create(scheme_no=sc_no, theory_cr=th_cr,practical_cr=pr_cr,max_th='0',max_mid='20',max_pr='80')


            elif th_cr=='1' and pr_cr=='1' or th_cr=='2' and pr_cr=='1' or th_cr=='2' and pr_cr=='2' or th_cr=='3' and pr_cr=='1' or th_cr=='3' and pr_cr=='2':
                Scheme= scheme.objects.create(scheme_no=sc_no, theory_cr=th_cr,practical_cr=pr_cr,max_th='50',max_mid='20',max_pr='30')

            elif th_cr=='1' and pr_cr=='2' or th_cr=='1' and pr_cr=='3' or th_cr=='1' and pr_cr=='4':
                Scheme= scheme.objects.create(scheme_no=sc_no, theory_cr=th_cr,practical_cr=pr_cr,max_th='30',max_mid='20',max_pr='50')


            else:
                return redirect(home,error_message="Enter a Valid Scheme!!")

            return redirect('home')

        else:
                return redirect('home')


def sub_form(request):
    if request.method=='POST':
        string=''
        string=str(request.POST['sub_no']) + str('/') + str(request.POST['student_scheme'])

        if subjects.objects.filter(sub_no=string).exists():
            return redirect(home,error_message="Subject Already Exist!!")


        Subject=subjects()
        Subject.sub_no=string
        Subject.sub_name=request.POST['sub_name']
        Subject.sub_stu_scheme=request.POST['student_scheme']
        sub_dept_no=request.POST['sub_dept_no']
        Subject.sub_dept_no=department.objects.get(dept_no=sub_dept_no)
        sub_scheme_no=request.POST['sub_scheme_no']
        Subject.sub_scheme_no=scheme.objects.get(scheme_no=sub_scheme_no)
        Subject.sem=request.POST['Sem']
        Subject.save()
        return redirect('home')

    else:
       return redirect('home')

def marks_form(request):
        if request.method=='POST':
            if student.objects.filter(enroll_no=request.POST['marks_enroll_no']).exists():

                        if backlog.objects.filter(back_enroll_no=request.POST['marks_enroll_no']).exists() and backlog.objects.filter(back_sub_no=request.POST['marks_sub_no']).exists():

                                back_obj=backlog.objects.get(back_enroll_no=request.POST['marks_enroll_no'])
                                field_name_back_sub='back_sub_no'
                                back_log_object=backlog._meta.get_field(field_name_back_sub)
                                back_log_sub_code=back_log_object.value_from_object(back_obj)



                                marks_sub_no=request.POST['marks_sub_no']
                                sub_scheme_obj=subjects.objects.get(sub_no=marks_sub_no)

                                field_name='sub_scheme_no'
                                field_object=subjects._meta.get_field(field_name)
                                scheme_id=field_object.value_from_object(sub_scheme_obj)

                                scheme_obj=scheme.objects.get(scheme_no=scheme_id)

                                field_name_th='theory_cr'
                                field_object_th=scheme._meta.get_field(field_name_th)
                                th_cr=field_object_th.value_from_object(scheme_obj)

                                field_name_pr='practical_cr'
                                field_object_pr=scheme._meta.get_field(field_name_pr)
                                pr_cr=field_object_pr.value_from_object(scheme_obj)

                                mark_back_obj=marks.objects.filter(marks_enroll_no=request.POST['marks_enroll_no']).filter(marks_sub_no=back_log_sub_code)
                                mark_back_obj.update(th=request.POST['th'])
                                mark_back_obj.update(pr=request.POST['pr'])
                                mark_back_obj.update(mid=request.POST['mid'])


                                result=(th_cr + pr_cr) * (int(request.POST['th']) + int(request.POST['pr']) + int(request.POST['mid']))/10
                                mark_back_obj.update(current_result=result)




                                if th_cr==1 and pr_cr==1 or th_cr==2 and pr_cr==1 or th_cr==2 and pr_cr==2 or th_cr==3 and pr_cr==1 or th_cr==3 and pr_cr==2:
                                    if (int(request.POST['th']) + int(request.POST['mid']))>=28 and int(request.POST['pr'])>=12:


                                        backlog.objects.get(back_enroll_no=request.POST['marks_enroll_no']).delete()



                                if th_cr==0 and pr_cr==1 or th_cr==0 and pr_cr==2 or th_cr==0 and pr_cr==3 or th_cr==0 and pr_cr==4:
                                    if int(request.POST['pr'])>=40:


                                        backlog.objects.get(back_enroll_no=request.POST['marks_enroll_no']).delete()


                                if th_cr==1 and pr_cr==0 or th_cr==2 and pr_cr==0 or th_cr==3 and pr_cr==0 or th_cr==4 and pr_cr==0:
                                    if (int(request.POST['th']) + int(request.POST['mid']))>=40:


                                        backlog.objects.get(back_enroll_no=request.POST['marks_enroll_no']).delete()


                                if th_cr==1 and pr_cr==2 or th_cr==1 and pr_cr==3 or th_cr==1 and pr_cr==4:
                                    if (int(request.POST['th']))>=12 or int(request.POST['pr'])>=28:


                                        backlog.objects.get(back_enroll_no=request.POST['marks_enroll_no']).delete()


                                return redirect(home,error_message='BackLog subject updated for current student')




                        else:
                                Marks=marks()

                                sub_obj=subjects.objects.get(sub_no=request.POST['marks_sub_no'])
                                field_name_subject='sub_no'
                                field_object_sub=subjects._meta.get_field(field_name_subject)
                                subject_no=str(field_object_sub.value_from_object(sub_obj))

                                sub_last_ele=(subject_no[0:5])
                                print(sub_last_ele)
                                sub_sare_list=subjects.objects.all().filter(sub_no__contains=sub_last_ele)

                                print(sub_sare_list)

                                student_roll=request.POST['marks_enroll_no']
                                student_start_four=int(student_roll[0:4])

                                print(student_start_four)
                                min=5
                                subject_loop_obj=subjects()

                                for subject in sub_sare_list:



                                    field_name_subject_loop='sub_no'
                                    field_object_sub_loop=subjects._meta.get_field(field_name_subject_loop)
                                    subject_no=str(field_object_sub.value_from_object(subject))
                                    sub_last_four_int=int(subject_no[-4:])
                                    print(sub_last_four_int)


                                    if (student_start_four-sub_last_four_int)<min:
                                        min=(student_start_four-sub_last_four_int)
                                        subject_loop_obj=subject

                                        print(min)





                                field_name_sub_no='sub_no'
                                field_object_sub_no=subjects._meta.get_field(field_name_sub_no)
                                sub_id=field_object_sub_no.value_from_object(subject_loop_obj)


                                Marks.marks_sub_no=subjects.objects.get(sub_no=sub_id)
                                sub_scheme_obj=subjects.objects.get(sub_no=sub_id)

                                field_name='sub_scheme_no'
                                field_object=subjects._meta.get_field(field_name)
                                scheme_id=field_object.value_from_object(sub_scheme_obj)

                                scheme_obj=scheme.objects.get(scheme_no=scheme_id)

                                field_name_th='theory_cr'
                                field_object_th=scheme._meta.get_field(field_name_th)
                                th_cr=field_object_th.value_from_object(scheme_obj)

                                field_name_pr='practical_cr'
                                field_object_pr=scheme._meta.get_field(field_name_pr)
                                pr_cr=field_object_pr.value_from_object(scheme_obj)

                                total_cr=th_cr + pr_cr
                                Marks.current_cr=total_cr

                                marks_enroll_no=request.POST['marks_enroll_no']
                                Marks.marks_enroll_no=student.objects.get(enroll_no=marks_enroll_no)
                                Marks.th=request.POST['th']
                                Marks.pr=request.POST['pr']
                                Marks.mid=request.POST['mid']

                                result=(th_cr + pr_cr) * (int(Marks.th) + int(Marks.pr) + int(Marks.mid))/10
                                Marks.current_result=result

                                if th_cr==1 and pr_cr==1 or th_cr==2 and pr_cr==1 or th_cr==2 and pr_cr==2 or th_cr==3 and pr_cr==1 or th_cr==3 and pr_cr==2:
                                    if (int(Marks.th) + int(Marks.mid))<28 or int(Marks.pr)<12:
                                        back=backlog()
                                        enroll=request.POST['marks_enroll_no']
                                        back.back_enroll_no=student.objects.get(enroll_no=enroll)
                                        back.back_sub_no=subjects.objects.get(sub_no=sub_id)
                                        back.save()

                                if th_cr==0 and pr_cr==1 or th_cr==0 and pr_cr==2 or th_cr==0 and pr_cr==3 or th_cr==0 and pr_cr==4:
                                    if int(Marks.pr)<40:
                                        back=backlog()
                                        enroll=request.POST['marks_enroll_no']
                                        back.back_enroll_no=student.objects.get(enroll_no=enroll)
                                        back.back_sub_no=subjects.objects.get(sub_no=marks_sub_no)
                                        back.save()

                                if th_cr==1 and pr_cr==0 or th_cr==2 and pr_cr==0 or th_cr==3 and pr_cr==0 or th_cr==4 and pr_cr==0:
                                    if (int(Marks.th) + int(Marks.mid))<40:
                                        back=backlog()
                                        enroll=request.POST['marks_enroll_no']
                                        back.back_enroll_no=student.objects.get(enroll_no=enroll)
                                        back.back_sub_no=subjects.objects.get(sub_no=marks_sub_no)
                                        back.save()

                                if th_cr==1 and pr_cr==2 or th_cr==1 and pr_cr==3 or th_cr==1 and pr_cr==4:
                                    if (int(Marks.th))<12 or int(Marks.pr)<28:
                                        back=backlog()
                                        enroll=request.POST['marks_enroll_no']
                                        back.back_enroll_no=student.objects.get(enroll_no=enroll)
                                        back.back_sub_no=subjects.objects.get(sub_no=marks_sub_no)
                                        back.save()

                                Marks.save()
                                return redirect('home')
            else:
                    return redirect(home,error_message="Student Does Not Exist!!")

        else:
                return render(request,'job/home.html',context)





def result_form(request):
    if request.method=='POST':
        if student.objects.filter(enroll_no=request.POST['result_enroll']).exists():
            student_object=student.objects.get(enroll_no=request.POST['result_enroll'])
            field_name_roll='enroll_no'
            field_object_result=student._meta.get_field(field_name_roll)
            roll_no=field_object_result.value_from_object(student_object)

            field_name_stu_scheme_year='student_scheme_year'
            field_object_stu_scheme=student._meta.get_field(field_name_stu_scheme_year)
            stu_scheme_year=str(field_object_stu_scheme.value_from_object(student_object))
            compare_scheme_code=int(stu_scheme_year[-4:])
            print(compare_scheme_code)
            result_sem_no=request.POST['Sem']
            sub_no_obj=subjects.objects.all().filter(sem=result_sem_no).filter(sub_stu_scheme=compare_scheme_code)

            Marks=marks.objects.all().filter(marks_enroll_no=roll_no).filter(marks_sub_no__in=sub_no_obj)
            result_sum=0
            result_cr=0
            result_t=0
            crs=0
            for mark in Marks:
                field_name_current_result='current_result'
                field_object_current_result=marks._meta.get_field(field_name_current_result)
                result_t=field_object_current_result.value_from_object(mark)

                result_sum+=result_t

                field_name_current_cr='current_cr'
                field_object_current_cr=marks._meta.get_field(field_name_current_cr)
                crs=field_object_current_cr.value_from_object(mark)

                result_cr+=crs

            fnl_result=float(result_sum/(result_cr))

            # if result.objects.filter(result_enroll_no=roll_no).exists():
            #     res_obj=result.objects.filter(result_enroll_no=roll_no)
            #
            #     if int(request.POST['Sem'])==1:
            #         if float(res_obj.sem1)!= 0:
            #             res_obj.update(sem1=fnl_result)
            #             res_obj.update(ogpa=fnl_result)
            #         else:
            #                         final_result=result()
            #                         final_result.result_enroll_no=student.objects.get(enroll_no=request.POST['result_enroll'])
            #                         final_result.sem1=fnl_result
            #                         final_result.ogpa=fnl_result
            #                         final_result.save()
            #     else:


            final_result=result()
            final_result.result_enroll_no=student.objects.get(enroll_no=request.POST['result_enroll'])
            final_result.sem1=fnl_result
            final_result.ogpa=fnl_result
            final_result.save()
            return redirect('home')
        else:
                return redirect(home,error_message="Student Does Not Exist!!")

    else:
            return redirect('home')
