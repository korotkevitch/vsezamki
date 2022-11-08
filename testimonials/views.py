from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Testimonial


class TestimonialView(ListView):
    model = Testimonial
    template_name = 'testimonials.html'
    context_object_name = 'all_testimonials'
