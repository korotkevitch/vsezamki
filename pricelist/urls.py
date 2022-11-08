from django.urls import path
from pricelist import views
from .views import PriceView


urlpatterns = [
    path('', PriceView.as_view(), name='price')

]