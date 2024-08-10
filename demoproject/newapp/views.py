from django.shortcuts import render, HttpResponsePermanentRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
from django.views import View
# Create your views here.


def index(request):
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path
    if request.method == 'POST':
        return HttpResponsePermanentRedirect(reverse('newapp:login'))
    # elif request.method == 'GET':
    return render(request, 'index.html', {'address': address, 'user_agent': user_agent, 'path': path})


def login(request):
    # if request.method == 'GET':
    #     return render(request, 'index.html')
    if request.method == 'POST':
        return HttpResponsePermanentRedirect(reverse('newapp:index'))
    return render(request, 'login.html')
    
