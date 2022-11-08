from django import forms
from django.forms import ModelForm, Textarea
from home.models import About, HomeArticleWithPhoto, HomeArticle


class AboutForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = About
        fields = '__all__'


class HomeArticleWithPhotoForm(ModelForm):

    class Meta:
        model = HomeArticle
        fields = '__all__'
        widgets = {
            'text': Textarea(attrs={'cols': 160,
                                    'rows': 20})
        }

class HomeArticleForm(ModelForm):

    class Meta:
        model = HomeArticle
        fields = '__all__'
        widgets = {
            'text': Textarea(attrs={'cols': 160,
                                    'rows': 20})
        }