from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    # so always ensure such a page(with slug) exists
]
