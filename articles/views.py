from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse

def article_list(request):
    return render(request, 'articles/articles_list.html')

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
