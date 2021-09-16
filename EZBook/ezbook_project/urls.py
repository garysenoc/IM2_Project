
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('index',views.StudentIndexView.as_view(), name="index."),

    path('', views.home,name='booking-home'),
    path('features/', views.features,name='booking-features'),
    path('signin/', views.signin,name='booking-signin'),
    path('register/', views.register,name='booking-register'),
    path('about/',views.about,name='booking-about'),
    path('contact/',views.contact,name='booking-contact')
]
