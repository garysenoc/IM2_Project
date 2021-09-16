from django.shortcuts import render
from django.views.generic import View, TemplateView

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