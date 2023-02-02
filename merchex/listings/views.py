
# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',context={"bands" : bands})
def contact(request):
    return render (request, 'listings/contact.html')
