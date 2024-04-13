from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

#def article_list(request):
#    return render(request, 'articles/articles_list.html')

def index(request):
    return HttpResponse('Hellow world')

def article_list(request):
    articles = Article.objects.all().order_by('date')  # getting the data from model/table
    return render(request, 'articles/articles_list.html',
                  {'articles': articles})  # 3rd(context) parameter is the data passed
    # to the template {'articles': articles}, can name dict ky anything


def article_detail(request, slug):
    # return render(request, 'articles/articles_about.html')
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url='/accounts/login/')  # decorator extends the function, adds additional functionality
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/create_article.html', {'form': form})

