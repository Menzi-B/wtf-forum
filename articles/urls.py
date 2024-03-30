from django.urls import path
from articles.views import views

app_name = 'articles'

urlpatterns = [
    path('', index),
    # so always ensure such a page(with slug) exists
]
