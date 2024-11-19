from django.shortcuts import render
from django.views import View
from dashboard.models import *
from menu.models import *
from django.db.models import Prefetch, Count


# Create your views here.
class FrontPageView(View):
    def get(self, request):
        menu = MenuItem.objects.all()[:4]

        return render(request, 'website/index.html', {
            'menu': menu,
        })

    
class BreakfastView(View):
    def get(self, request):
        return render(request, 'website/pages/breakfast.html')
    
class LunchView(View):
    def get(self, request):
        return render(request, 'website/pages/lunch.html')
    
class DinnerView(View):
    def get(self, request):
        return render(request, 'website/pages/dinner.html')
    
class DrinksView(View):
    def get(self, request):
        return render(request, 'website/pages/drinks.html')
    
class AboutUsView(View):
    def get(self, request):
        return render(request, 'website/pages/aboutus.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'website/pages/contact.html')
