from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render (request,'FIRSTAPPLICATION/homepage.html')

def firstpage(request):
    return render (request,'FIRSTAPPLICATION/firstpage.html')


    

    
    