from django.contrib import admin
from .models import Classroom, StudentClassroom, TeacherClassroom

# Register your models here.
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('className', 'courseID', 'teacher', 'classTeacherMail', 'classCode')

class StudentClassroomAdmin(admin.ModelAdmin):
    list_display = ('studentEmail',)

class TeacherClassroomAdmin(admin.ModelAdmin):
    list_display = ('teacherEmail',)

admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(StudentClassroom, StudentClassroomAdmin)
admin.site.register(TeacherClassroom, TeacherClassroomAdmin )
