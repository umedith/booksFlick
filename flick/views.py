from django.shortcuts import render,redirect

from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def search_results(request):
#   
       return render(request, 'all-apps/search.html',{"message":message})