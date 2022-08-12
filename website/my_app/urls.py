from django.contrib import admin
from django.urls import path
from my_app.apps import MyAppConfig
from my_app import views

app_name = MyAppConfig.name

urlpatterns = [
    path('', views.index, name='index' ),
    path('home/', views.home, name='home' ),
    path('stuinfo/', views.student_details, name='student_details' ),
    path('apioverview/', views.apioverview, name='apioverview' ),
    path('taskupdate/', views.taskupdate, name='taskupdate' ),
    path('taskdelete/', views.taskdelete, name='taskdelete' ),
    

  
]

