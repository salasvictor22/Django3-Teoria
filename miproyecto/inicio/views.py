from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myHomeView(request, *args, **kwargs):
    myContext = {
        'myText': 'Esto es sobre nosotros',
        'myNumber': 123,
        'myList': [33, 44, 55],
    }
    return render(request, "home.html", myContext)
   
def myPersonalView(request, *args, **kwargs):
    return render(request, "personal.html", {})
    
def anotherView(request):
   return HttpResponse('<h1>Solo otra pagina</h1>') 