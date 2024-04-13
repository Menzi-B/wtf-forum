from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta: #  define how we want to output our form , which fields and from which model(table) do we inherit these fields from
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumbnail']
