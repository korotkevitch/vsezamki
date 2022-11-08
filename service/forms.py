from django import forms
from django.forms import ModelForm, Textarea
from service.models import ServiceListArticle, ServiceDetailArticle


class ServiceListArticleForm(ModelForm):

    class Meta:
        model = ServiceListArticle
        fields = '__all__'
        widgets = {
            'text': Textarea(attrs={'cols': 160,
                                    'rows': 20})
        }


class ServiceDetailArticleForm(ModelForm):

    class Meta:
        model = ServiceDetailArticle
        fields = '__all__'
        widgets = {
            'text': Textarea(attrs={'cols': 160,
                                    'rows': 20})
        }