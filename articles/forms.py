from django import forms
from django.forms import ModelForm, Textarea
from articles.models import ArticleList, ArticleDetail


class ArticleListForm(ModelForm):

    class Meta:
        model = ArticleList
        fields = '__all__'
        widgets = {
            'text': Textarea(attrs={'cols': 160,
                                    'rows': 20},)
        }


class ArticleDetailForm(ModelForm):

    class Meta:
        model = ArticleDetail
        fields = '__all__'
        widgets = {
            'text': Textarea(attrs={'cols': 160,
                                    'rows': 20})
        }
