from django.urls import path
from articles import views
from .views import ArticleListView, ArticleDetailView


urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
    path('<slug:service_slug>/<slug:article_slug>/', ArticleDetailView.as_view(), name='article_details'),
]