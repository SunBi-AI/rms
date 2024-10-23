from django.shortcuts import render
from django.views import View
from dashboard.models import *
from menu.models import *
from django.db.models import Prefetch, Count


# Create your views here.
class FrontPageView(View):
    def get(self, request):
        menu = MenuItem.objects.all()[:4]  
        settings = SiteSettings.objects.first() 
        about_settings = AboutSettings.objects.first()

        context = {
            'settings': settings,
            'menu': menu,
            'about_settings': about_settings
        }

        return render(request, 'website/index.html', context)

    
class BreakfastView(View):
    def get(self, request):
        breakfast_items = MenuItem.objects.filter(items_category__name__iexact='breakfast')
        context = {
            'breakfast_items': breakfast_items
        }
        return render(request, 'website/pages/breakfast.html', context)
    
class LunchView(View):
    def get(self, request):
        lunch_items = MenuItem.objects.filter(items_category__name__iexact='lunch')  # Case-insensitive check
        context = {
            'lunch_items': lunch_items
        }
        return render(request, 'website/pages/lunch.html', context)

    
class DinnerView(View):
    def get(self, request):
        dinner_items = MenuItem.objects.filter(items_category__name__iexact='dinner')  # Case-insensitive check
        context = {
            'dinner_items': dinner_items
        }
        return render(request, 'website/pages/dinner.html', context)

    
class DrinksView(View):
    def get(self, request):
        drinks_items = MenuItem.objects.filter(items_category__name__iexact='drinks')  # Case-insensitive check
        context = {
            'drinks_items': drinks_items
        }
        return render(request, 'website/pages/drinks.html', context)

    
class AboutUsView(View):
    def get(self, request):
        about_settings = AboutSettings.objects.first() 
        context = {
            'about_settings': about_settings
        }
        return render(request, 'website/pages/aboutus.html', context)


class ContactView(View):
    def get(self, request):
        return render(request, 'website/pages/contact.html')
