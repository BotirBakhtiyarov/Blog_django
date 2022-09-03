from django import forms
from . import models

from django_summernote.widgets import SummernoteWidget

class BlogCreateViewForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','body','author']

    body = forms.CharField(widget=SummernoteWidget)

class BlogUpdateViewForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','body']

    body = forms.CharField(widget=SummernoteWidget)
