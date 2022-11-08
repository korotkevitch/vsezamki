from django.urls import path
from service import views
from .views import ServiceListView, ServiceDetailView


urlpatterns = [
    path('', ServiceListView.as_view(), name='services'),
    path('<slug:service_slug>/', ServiceDetailView.as_view(), name='service_details'),
]