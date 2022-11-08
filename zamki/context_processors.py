from service.models import ServiceDetail
from articles.models import ArticleDetail
from contact.models import Contact


def all_services(request):
    return {'all_services': ServiceDetail.objects.all()}


def all_articles(request):
    return {'all_articles': ArticleDetail.objects.all().order_by('-created_date').filter(is_activated=True)}


def three_articles(request):
    return {'three_articles': ArticleDetail.objects.all().filter(is_activated=True).order_by('-created_date')[:3]}


def contact(request):
    return {'contact': Contact.objects.all()}