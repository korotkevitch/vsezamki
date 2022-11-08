from django.urls import path
from testimonials import views
from .views import TestimonialView


urlpatterns = [
    path('', TestimonialView.as_view(), name='testimonials'),
]