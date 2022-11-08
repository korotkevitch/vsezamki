from django.urls import path
from contact import views
from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]