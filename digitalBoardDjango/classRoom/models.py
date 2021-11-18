from django.db import models

# Create your models here.
class Classroom(models.Model):
    className = models.CharField(max_length=100)
    courseID = models.CharField(max_length=50)
    teacher =  models.EmailField(max_length=100)
    classTeacherMail = models.CharField(max_length=254, primary_key=True)
    classCode = models.CharField(max_length=10)

class StudentClassroom(models.Model):
    studentEmail =  models.EmailField(max_length=254, primary_key=True)
    classTeacherMail = models.ManyToManyField(Classroom)

class TeacherClassroom(models.Model):
    teacherEmail =  models.EmailField(max_length=254, primary_key=True)
    classTeacherMail = models.ManyToManyField(Classroom)