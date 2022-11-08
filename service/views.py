from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView
from .models import ServiceDetail, ServiceListArticle, ServiceDetailArticle
from articles.models import ArticleDetail


class ServiceListView(ListView):
    model = ServiceDetail
    template_name = 'services.html'
    context_object_name = 'all_services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['service_list_articles'] = ServiceListArticle.objects.all().filter(is_activated=True)
        return context

class ServiceDetailView(ListView):
    template_name = 'service_details.html'
    context_object_name = 'current_service_details'

    def get_queryset(self):
        return get_object_or_404(ServiceDetail, slug=self.kwargs['service_slug'])

    def get_context_data(self, **kwargs):
        self.service = get_object_or_404(ServiceDetail, slug=self.kwargs['service_slug'])
        context = super().get_context_data()
        context['service_detail_articles'] = ServiceDetailArticle.objects.filter(service=self.service).filter(is_activated=True)
        context['service_articles'] = ArticleDetail.objects.filter(service=self.service).filter(is_activated=True)
        return context

