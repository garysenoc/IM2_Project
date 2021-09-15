
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('index',views.StudentIndexView.as_view(), name="index."),
]
