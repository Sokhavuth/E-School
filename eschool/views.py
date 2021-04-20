from django.shortcuts import render
from django.http import HttpResponse

context = {'site_title': 'E-School'}

def index(request):
    return render(request, 'index.html', context=context)