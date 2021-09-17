from django.shortcuts import render
from django.views.generic import View
from ezbook_project.models import User, Company, Driver, Vehicle,Travel_Places,BookTravel,Booking

# Create your views here.

class StudentIndexView(View):
    def get(self,request):
        return render(request, 'home.html')

def home(request):
    return render(request,'home.html')
def about(request):
   return render(request,'about.html',{'title':'about'})
def features(request):
     return render(request,'features.html',{'title':'features'})
def signin(request):
    return render(request,'signin.html',{'title':'signin'})
def register(request):
    return render(request,'register.html',{'title':'register'})
def contact(request):
    return render(request,'contact.html',{'title':'contact'})

def dashboard(request):
    users = User.objects.all()
    return render(request,'dashboard.html',{'users':users})
def dashboard_company(request):
    companies = Company.objects.all()
    return render(request,'dashboard_companies.html',{'companies':companies})

def dashboard_driver(request):
    drivers = Driver.objects.all()
    return render(request,'dashboard_drivers.html',{'drivers':drivers})

def dashboard_vehicle(request):
    vehicles = Vehicle.objects.all()
    return render(request,'dashboard_vehicle.html',{'vehicles':vehicles})

def dashboard_travelplaces(request):
    travel_places = Travel_Places.objects.all()
    return render(request,'dashboard_travelplaces.html',{'travel_places':travel_places})

def dashboard_booktravel(request):
    available_bookings = BookTravel.objects.all()
    return render(request,'dashboard_availablebookings.html',{'available_bookings':available_bookings})

def dashboard_booking(request):
    bookings = Booking.objects.all()
    return render(request,'dashboard_bookings.html',{'bookings':bookings})