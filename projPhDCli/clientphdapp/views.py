from django.shortcuts import render
from django.http import HttpResponse

def vodhome(request):
    template = 'clientphdapp/vodclient.html'
    return render(request, template, {'videos': 'videos'})
# Create your views here.
