from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Head, About, Principle, VideoBlock, HomeArticleWithPhoto, HomeArticle


class HomeView(ListView):
    model = Head
    template_name = 'index.html'
    context_object_name = 'head'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['about'] = About.objects.all()
        context['principles'] = Principle.objects.all()
        context['videoblock'] = VideoBlock.objects.all()
        context['home_article_with_photo'] = HomeArticleWithPhoto.objects.all()
        context['home_article'] = HomeArticle.objects.all().filter(is_activated=True)
        return context
