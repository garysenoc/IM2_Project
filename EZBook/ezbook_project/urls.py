
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views, admin_views

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
    path('ezbook_admin/', include([
        path('', admin_views.dashboard),
        path('tables/', include([
            path('users', admin_views.users),
            path('companies', admin_views.companies),
            path('drivers', admin_views.drivers),
            path('vehicles', admin_views.vehicles),
            path('travelplaces', admin_views.travelplaces),
            path('bookings', admin_views.bookings),
            path('availablebookings', admin_views.availablebookings),
        ]))
    ])),

    #     path('dashboard/companies', views.dashboard_company,
    #          name='dashboard-companies'),
    #     path('dashboard/drivers', views.dashboard_driver, name='dashboard-driver'),
    #     path('dashboard/vehicle', views.dashboard_vehicle, name='dashboard-vehicle'),
    #     path('dashboard/travel', views.dashboard_travelplaces, name='dashboard-travel'),
    #     path('dashboard/bookings', views.dashboard_booking, name='dashboard-booking'),
    #     path('dashboard/available_bookings', views.dashboard_booktravel,
    #          name='dashboard-available_bookings'),
]
