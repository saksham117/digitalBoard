from __future__ import print_function
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import CreateClassRoom
from .models import Classroom, StudentClassroom, TeacherClassroom

# for generating the class code
import random
import string

# creating a set having global scope, sotring all unique classCodes we have encountered
setOfClassCodes = set()



# helper functions
def getClassCode(length):
    # With combination of lower and upper case and digits
    characters = string.ascii_letters + string.digits
    classCode = ''.join(random.choice(characters) for i in range(length))
    # print random string
    print(classCode)
    return classCode

def print_user_details(request):
    user = request.user
    print(user.username)
    print(user.email)


# Create your views here.
def index(request):
    return render(request, "index.html")

def classRoom(request):
    if request.user.is_authenticated:
        teacherEMail = request.user.email
        # result = TeacherClassroom.objects.get(pk = teacherEMail)
        # 
        # if result:
        listOfClasses = []
        try:
            obj = TeacherClassroom.objects.get(pk = teacherEMail)
            print(obj)
            print(list(obj.classTeacherMail.all()))
            listOfClasses = list(obj.classTeacherMail.all())
        except:
            print("No classrooms exist yet")    

        return render(request, 'classRoom.html', {
                                                   'listOfClasses': listOfClasses,
                                                 })
    else:
        return HttpResponseRedirect('/login/')

def createClass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = CreateClassRoom(request.POST)
            if fm.is_valid():

                # filtering out the data received from the form
                className = fm.cleaned_data['class_Name']
                courseID = fm.cleaned_data['course_ID']
                # getting the mail id of user which is attached to the request
                teacher = request.user.email
                # creating the primary key using mailid of teacher and nameofclass
                primaryKey = className + "_" + teacher
                # generating the classcode of length 6
                classCode = getClassCode(6)

                # checking if this class code has already been used or not
                # if used generate a new unique classcode
                if classCode in setOfClassCodes:
                    while(classCode in setOfClassCodes):
                        classCode = getClassCode(6)
                
                # add the new unique key to setof classcodes
                setOfClassCodes.add(classCode)

                # making an entry into the database of classrooms
                obj = Classroom(className = className,
                                  courseID = courseID,
                                  classCode = classCode,
                                  teacher = teacher,
                                  classTeacherMail = primaryKey)
                obj.save()

                # adding this particular classroom to the list of classrooms taught by that particular teacher
                # whose session is active
                teacherObj = TeacherClassroom(teacherEmail = teacher)
                teacherObj.save()
                teacherObj.classTeacherMail.add(obj)
                teacherObj.save()

                return HttpResponseRedirect('/classroom/')
        else:
            fm = CreateClassRoom()
            return render(request, 'createClass.html', {'form': fm,})
    else:
        return HttpResponseRedirect('/login/')
