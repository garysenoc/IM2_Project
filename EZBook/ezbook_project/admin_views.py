from django.shortcuts import render


base_title = 'EZBook Admin'


def dashboard(request):
    # users = User.objects.all()
    return render(request, 'ezbook_admin/index.html', {'title': f'{base_title} - Dashboard'})


def users(request):
    return render(request, 'ezbook_admin/users.html', {'title': f'{base_title} - Users'})


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
