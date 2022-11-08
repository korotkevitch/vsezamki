from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView
from .models import ArticleDetail, ArticleList
from service.models import ServiceDetail


class ArticleListView(ListView):
    model = ArticleDetail
    template_name = 'articles.html'
    context_object_name = 'all_articles'

    def get_queryset(self):
        return ArticleDetail.objects.all().order_by('-created_date').filter(is_activated=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['articles_list'] = ArticleList.objects.all()
        return context

class ArticleDetailView(ListView):
    template_name = 'article_details.html'
    context_object_name = 'current_article'

    def get_queryset(self):
        return get_object_or_404(ArticleDetail, slug=self.kwargs['article_slug'], is_activated=True)

    def get_context_data(self, **kwargs):
        self.service = get_object_or_404(ServiceDetail, slug=self.kwargs['service_slug'])
        context = super().get_context_data()
        context['service_articles'] = ArticleDetail.objects.filter(service=self.service)
        context['current_service'] = self.service
        context['other_service_articles'] = ArticleDetail.objects.filter(service=self.service).filter(is_activated=True).\
            exclude(slug=self.kwargs['article_slug'])
        return context

