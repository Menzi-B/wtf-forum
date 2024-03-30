from django.shortcuts import render, redirect
from django.http import HttpResponse

def article_list(request):
    return render(request, 'articles/articles_list.html')
