from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.static import serve
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('classroom/', views.classRoom, name='classroom'),
    path('createclass/', views.createClass, name='createclass'),

]
