from django.shortcuts import render
from ezbook_project.models import User, Company, Driver, Vehicle, Travel_Places, BookTravel, Booking
from ezbook_project.forms import UserForm
import json
from django.core.serializers.json import DjangoJSONEncoder
base_title = 'EZBook Admin'


def dashboard(request):
    count = {
       "user_count" : User.objects.all().count(),
       "bookings_count" : Booking.objects.all().count(),
       "company_count" : Company.objects.all().count(),
       "driver_count" : Driver.objects.all().count(),
       "vehicle_count" : Vehicle.objects.all().count(),
    }

    data = Booking.objects.raw("SELECT 1 as id, COUNT(ID) as total, booking_date FROM heroku_edd82c657812381.ezbook_project_booking group by booking_date")
    
    date = []
    num = []
    for i in data:
        date.append((i.booking_date))
        num.append(i.total)
    
    return render(request, 'ezbook_admin/index.html', {'title': f'{base_title} - Dashboard','count' : count,'date': json.dumps(date,cls=DjangoJSONEncoder),'num':json.dumps(num)})


def users(request):
    if request.method != 'POST':
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            firstname = request.POST.get('firstname')
            middlename = request.POST.get('middlename')
            lastname = request.POST.get('lastname')
            age = request.POST.get('age')
            phone_number = request.POST.get('phone_number')
            email = request.POST.get('email')
            form = User(
                username=username,
                firstname=firstname,
                middlename=middlename,
                lastname=lastname,
                age=age,
                phone_number=phone_number,
                email=email,
            )
            print('HERE: ', form)
    users = User.objects.all()
    return render(request, 'ezbook_admin/tables/users.html', {'title': f'{base_title} - Users', 'users': users, 'form': form})


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
