from django.shortcuts import render
from ezbook_project.models import User, Company, Driver, Vehicle, Travel_Places, BookTravel, Booking


base_title = 'EZBook Admin'


def dashboard(request):
    return render(request, 'ezbook_admin/index.html', {'title': f'{base_title} - Dashboard'})


def users(request):
    users = User.objects.all()
    return render(request, 'ezbook_admin/tables/users.html', {'title': f'{base_title} - Users', 'users': users})


def companies(request):
    companies = Company.objects.all()
    return render(request, 'ezbook_admin/tables/companies.html', {'title': f'{base_title} - Companies', 'companies': companies})


def drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'ezbook_admin/tables/drivers.html', {'title': f'{base_title} - Drivers', 'drivers': drivers})


def vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'ezbook_admin/tables/vehicles.html', {'title': f'{base_title} - Vehicles', 'vehicles': vehicles})


def travelplaces(request):
    travel_places = Travel_Places.objects.all()
    return render(request, 'ezbook_admin/tables/travelplaces.html', {'title': f'{base_title} - Travel Places', 'travel_places': travel_places})


def bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'ezbook_admin/tables/bookings.html', {'title': f'{base_title} - Bookings', 'bookings': bookings})


def availablebookings(request):
    available_bookings = BookTravel.objects.all()
    return render(request, 'ezbook_admin/tables/availablebookings.html', {'title': f'{base_title} - Available Bookings', 'available_bookings': available_bookings})


# def dashboard_company(request):
#     companies = Company.objects.all()
#     return render(request, 'dashboard_companies.html', {'companies': companies})


# def dashboard_driver(request):
#     drivers = Driver.objects.all()
#     return render(request, 'dashboard_drivers.html', {'drivers': drivers})


# def dashboard_vehicle(request):
#     vehicles = Vehicle.objects.all()
#     return render(request, 'dashboard_vehicle.html', {'vehicles': vehicles})


# def dashboard_travelplaces(request):
#     travel_places = Travel_Places.objects.all()
#     return render(request, 'dashboard_travelplaces.html', {'travel_places': travel_places})


# def dashboard_booktravel(request):
#     available_bookings = BookTravel.objects.all()
#     return render(request, 'dashboard_availablebookings.html', {'available_bookings': available_bookings})


# def dashboard_booking(request):
#     bookings = Booking.objects.all()
#     return render(request, 'dashboard_bookings.html', {'bookings': bookings})
