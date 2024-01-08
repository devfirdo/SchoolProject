
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('tsignup',views.tsignup,name='tsignup'),
    path('main_login',views.main_login,name='main_login'),
    path('add_course',views.add_course,name='add_course'),
    path('course_insertion',views.course_insertion,name='course_insertion'),
    path('add_student',views.add_student,name='add_student'),
    path('student_insertion',views.student_insertion,name='student_insertion'),
    path('std_details',views.std_details,name='std_details'),
    path('std_delete/<int:pk>',views.std_delete,name='std_delete'),
    path('std_edit/<int:pk>',views.std_edit,name='std_edit'),
    path('student_updation/<int:pk>',views.student_updation,name='student_updation'),
    path('teacher_registration',views.teacher_registration,name='teacher_registration'),
    path('teacher_profile',views.teacher_profile,name='teacher_profile'),
    path('teacher_page',views.teacher_page,name='teacher_page'),
    path('teacher_edit',views.teacher_edit,name='teacher_edit'),
    path('teacher_update',views.teacher_update,name='teacher_update'),
    path('teacher_details',views.teacher_details,name='teacher_details'),
    path('teacher_delete/<int:pk>',views.teacher_delete,name='teacher_delete'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('teacher_home',views.teacher_home,name='teacher_home'),
    path('teacher_logout',views.teacher_logout,name='teacher_logout'),
    
]
