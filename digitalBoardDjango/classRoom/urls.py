from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.static import serve
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('aboutus/', views.aboutUs, name='aboutus'),
    path('classroom/', views.classRoom, name='classroom'),
    path('createclass/', views.createClass, name='createclass'),
    path('joinclass/', views.joinClass, name='joinclass'),
    path('requestaccess/', views.sendEmail, name='requestaccess'),
    path('classroomcontent/<str:classId>/', views.viewClassRoom, name='classroomcontent'),
    path('classroomcontent/<str:classId>/createassignment/', views.createAssignment, name='createassignment'),
    path('classroomcontent/<str:classId>/<str:taskCode>/', views.submitAssignment, name='submitassignment'),
    path('classroomcontent/<str:classId>/<str:taskCode>/viewsubmissions', views.viewSubmissions, name='viewSubmissions'),


]
