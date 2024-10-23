from django.urls import path
from .views import FrontPageView,BreakfastView, LunchView, DinnerView, DrinksView, AboutUsView, ContactView

app_name = "core"

urlpatterns = [
    path('indexxx', FrontPageView.as_view(), name="index"),
    path('breakfast/', BreakfastView.as_view(), name="breakfast"),
    path('lunch/', LunchView.as_view(), name="lunch"),
    path('dinner/', DinnerView.as_view(), name="dinner"),
    path('drinks/', DrinksView.as_view(), name="drinks"),
    path('about/', AboutUsView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
]