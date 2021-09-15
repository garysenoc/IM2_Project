from django.shortcuts import render
from django.views.generic import View, TemplateView
# Create your views here.

class StudentIndexView(View):
    def get(self,request):
        return render(request, 'ezbook_project/home.html')