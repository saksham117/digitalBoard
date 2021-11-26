from django.db import models
from datetime import date

# Create your models here.
# The classroom table contains a list of all the classes that have been created so far
# the field classTeacherMail is a primary key and is formed by concatenating className with email id of teacher who created it
class Classroom(models.Model):
    className = models.CharField(max_length=100)
    courseID = models.CharField(max_length=50)
    teacher =  models.EmailField(max_length=100)
    classTeacherMail = models.CharField(max_length=254, primary_key=True)
    classCode = models.CharField(max_length=10, unique=True)

# This stores a list of all the student email ids and classTeacherMail is a foreign key connecting it with the Classroom table
# this basically allows us to map that what all classes do the students study in
class StudentClassroom(models.Model):
    studentEmail =  models.EmailField(max_length=254, primary_key=True)
    classTeacherMail = models.ManyToManyField(Classroom)


# This stores a list of all the teacher email ids and classTeacherMail is a foreign key connecting it with the Classroom table
# this basically allows us to map that what all classes do the teachers teach in
class TeacherClassroom(models.Model):
    teacherEmail =  models.EmailField(max_length=254, primary_key=True)
    classTeacherMail = models.ManyToManyField(Classroom)

# this maintains a list of all the classcodes used by now
class ClassCodes(models.Model):
    classCode = models.CharField(max_length=10, unique=True)

# model to store all the assignment uploaded as of now
# linked with classroom model via many to one relationship
class CreateAssignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    submissionDate = models.DateField()
    assignmentCode = models.CharField(max_length=10)
    attachments = models.FileField(max_length=200, blank=True)
    classroom = models.ForeignKey(Classroom, null=True, on_delete=models.SET_NULL)

# this maintains a list of all the assignment codes used by now
class AssignmentCodes(models.Model):
    assignmentCode = models.CharField(max_length=10, unique=True)


class SubmitAssignment(models.Model):
    studentEmail =  models.EmailField()
    attachments = models.FileField(max_length=200)
    assignment = models.ForeignKey(CreateAssignment, null=True, on_delete=models.SET_NULL)
    submissionDate = models.DateField(default=date.today)
    comment = models.TextField(null=True)
    studentEmailAssignmentCode = models.CharField(max_length=254, primary_key=True)
