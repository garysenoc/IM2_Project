
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ezbook'

urlpatterns = [
    path('index', views.StudentIndexView.as_view(), name="index."),

    path('', views.home, name='booking-home'),
    path('features/', views.features, name='booking-features'),
    path('signin/', views.signin, name='booking-signin'),
    path('register/', views.register, name='booking-register'),
    path('about/', views.about, name='booking-about'),
    path('contact/', views.contact, name='booking-contact'),
    path('about/', views.about, name='booking-about'),
    path('ezbook_admin/', views.ezbook_admin, name='booking-dashboard'),

#     path('dashboard/companies', views.dashboard_company,
#          name='dashboard-companies'),
#     path('dashboard/drivers', views.dashboard_driver, name='dashboard-driver'),
#     path('dashboard/vehicle', views.dashboard_vehicle, name='dashboard-vehicle'),
#     path('dashboard/travel', views.dashboard_travelplaces, name='dashboard-travel'),
#     path('dashboard/bookings', views.dashboard_booking, name='dashboard-booking'),
#     path('dashboard/available_bookings', views.dashboard_booktravel,
#          name='dashboard-available_bookings'),
]
