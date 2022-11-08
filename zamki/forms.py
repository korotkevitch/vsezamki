from django import forms
from django.forms import ModelForm, Textarea
from zamki.models import Article


# class ArticleForm(ModelForm):
#
#     class Meta:
#         model = Article
#         fields = '__all__'
#         widgets = {
#             'text': Textarea(attrs={'cols': 160, 'rows': 20})
#         }