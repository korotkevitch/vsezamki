from django.urls import path
from service import views
from .views import ContactFormView
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='contact.html')),
    path('contact_form', ContactFormView.as_view(), name="contact_form"),
    path('thanks', TemplateView.as_view(template_name='thanks.html')),
]