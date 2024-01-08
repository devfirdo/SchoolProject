from django.shortcuts import render,redirect
from django.db import IntegrityError
from SchoolApp.models import Student
from SchoolApp.models import Course
from SchoolApp.models import Teachers
from django.conf import settings
from django.contrib.auth.models import User,auth
from django.contrib import messages
import os

def home(request):
    return render(request,'home.html')

def tsignup(request):
    crss = Course.objects.all()
    return render(request,'teachers/signup.html',{'crs':crss}) 


def main_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        usr = auth.authenticate(username=username,password=password)
        if usr is not None:
            if usr.is_staff:
                auth.login(request,usr)
                return render(request,'admin/admin_page.html')
            else:
                auth.login(request,usr)
                return render(request,'teachers/teacher_page.html',{'usr':usr})
        else:
            messages.error(request,'Invalid Username or Password')
            return redirect('/')

def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, 'admin/admin_page.html')

def add_course(request):
    if request.user.is_authenticated:
        return render(request,'admin/add_course.html')
        
def course_insertion(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            coursename = request.POST.get('cname')
            coursefee = request.POST.get('cfee')
            crs = Course(course_name=coursename,course_fee=coursefee)
            crs.save()
            messages.success(request, 'Course added successfully')
            return redirect('add_course')

def add_student(request):
    if request.user.is_authenticated:
        crss = Course.objects.all()
        return render(request,'admin/add_student.html',{'crs':crss})

def student_insertion(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('sname')
            age = request.POST.get('sage')
            email = request.POST.get('smail')
            date = request.POST.get('sdate')
            crs_name = request.POST.get('sel')
            crs = Course.objects.get(id=crs_name)
            stu = Student(student_course=crs,student_name=name,student_age=age,student_email=email,student_joining_date=date)
            stu.save()
            return redirect('std_details')


def std_details(request):
    if request.user.is_authenticated:
        stdnt = Student.objects.all()
        return render(request,'admin/student_details.html',{'std':stdnt})   

def std_delete(request,pk):
    stu = Student.objects.get(id=pk)
    stu.delete()
    return redirect('std_details') 

def std_edit(request,pk):
    stdnt = Student.objects.get(id=pk)
    crss = Course.objects.all()
    return render(request,'admin/student_edit.html',{'std':stdnt, 'crs':crss})  

def student_updation(request,pk):   
    if request.method == 'POST':
        stu = Student.objects.get(id=pk)
        name = request.POST.get('sname')
        age = request.POST.get('sage')
        email = request.POST.get('smail')
        date = request.POST.get('sdate')
        crs_name = request.POST.get('sel')
        crs = Course.objects.get(id=crs_name)
        stu.student_name = name
        stu.student_age = age
        stu.student_email = email
        stu.student_joining_date = date
        stu.student_course = crs
        stu.save()
        return redirect('std_details')
    

def teacher_registration(request):
    if request.method == 'POST':
        fname = request.POST.get('tfname')
        lname = request.POST.get('tlname')
        uname = request.POST.get('tuname')
        password = request.POST.get('tpass')
        cpassword = request.POST.get('tcpass')
        age = request.POST.get('tage')
        mail = request.POST.get('temail')  
        address = request.POST.get('taddress')
        number = request.POST.get('tnum')
        image = request.FILES.get('timage')
        course = request.POST.get('course')
        if password == cpassword:
            if User.objects.filter(username=uname).exists():
                messages.error(request,'User name already exists')
                return redirect('tsignup')
            else:
                usr = User.objects.create_user(
                                    username = uname,
                                    password = password,
                                    first_name = fname,
                                    last_name = lname,
                                    email=mail
                                )
                usr.save()
                tcourse = Course.objects.get(id=course)
                tcr = Teachers(
                                teacher_name = usr,
                                teacher_course = tcourse,
                                teacher_age = age,
                                teacher_address = address,
                                teacher_number = number,
                                teacher_image = image
                            )
                tcr.save()
                messages.success(request,'Registration Successfull')
                return redirect('tsignup')
        else:
            messages.error(request,'Passwords do not match')
            return redirect('tsignup')
        
def teacher_page(request):
    if request.user.is_authenticated:
        return render(request,'teachers/teacher_page.html')
    
def teacher_home(request):
    if request.user.is_authenticated:
        return redirect('teacher_page')

def teacher_profile(request):
    if request.user.is_authenticated:
        curent_user = request.user.id
        tcrs = Teachers.objects.get(teacher_name=curent_user)
        return render(request,'teachers/teacher_profile.html',{'tcr':tcrs})

    
def teacher_edit(request):
    if request.user.is_authenticated:
        curent_user = request.user.id
        csr = Course.objects.all()
        tcrs = Teachers.objects.get(teacher_name=curent_user)
        return render(request,'teachers/teacher_edit.html',{'tcr':tcrs,'csr':csr})
    
def teacher_update(request):
    if request.user.is_authenticated:
        current_user = request.user.id
        tcr = Teachers.objects.get(teacher_name=current_user)
        usr = User.objects.get(id =current_user)
        if request.method == 'POST':
            try:
                usr.first_name = request.POST.get('tfname')
                usr.last_name = request.POST.get('tlname')
                usr.username = request.POST.get('tuname')
                tcr.teacher_age = request.POST.get('tage')
                usr.email = request.POST.get('temail')   
                tcr.teacher_address = request.POST.get('taddress')
                tcr.teacher_number = request.POST.get('tnumber')
                selected_course_id = request.POST.get('course')
                selected_course = Course.objects.get(id=selected_course_id)
                tcr.teacher_course = selected_course
                
                if len(request.FILES)!=0:
                    if len(tcr.teacher_image)>0:
                        os.remove(tcr.teacher_image.path)
                    tcr.teacher_image = request.FILES.get('timage')
                tcr.save()
                usr.save()
            except IntegrityError:
                messages.error(request, 'Username already exists')
                return redirect('teacher_edit')
            return redirect('teacher_profile')
        
        
def teacher_details(request):
    if request.user.is_authenticated:
        usr = User.objects.all()
        tcr = Teachers.objects.all()
        return render(request,'admin/admin_teacher_details.html',{'usr':usr,'tcr':tcr})
        
def teacher_delete(request, pk):
    tcr = Teachers.objects.get(id=pk)
    user = User.objects.get(username=tcr.teacher_name.username)
    tcr.delete()
    user.delete()

    return redirect('teacher_details')

def admin_logout(request):
    auth.logout(request)
    return redirect('home')

def teacher_logout(request):
    auth.logout(request)
    return redirect('home') 
    


        
        
        
            
