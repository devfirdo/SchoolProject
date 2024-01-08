from django.db import models
from django.contrib.auth.models import User,auth

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_fee = models.IntegerField()
    def __str__(self):
        return self.course_name
    
class Student(models.Model):
    student_course = models.ForeignKey(Course,on_delete=models.CASCADE) 
    student_name = models.CharField(max_length=255) 
    student_age = models.IntegerField() 
    student_email = models.EmailField()
    student_joining_date = models.DateField()
    def __str__(self):
        return self.student_name
    
class Teachers(models.Model):
    teacher_name = models.ForeignKey(User,on_delete=models.CASCADE)
    teacher_course = models.ForeignKey(Course,on_delete=models.CASCADE) 
    teacher_age = models.IntegerField() 
    teacher_address = models.CharField(max_length=255) 
    teacher_number = models.IntegerField()
    teacher_image = models.ImageField(upload_to='image/',blank=True)
    def __str__(self):
        return self.teacher_address
    
    
    