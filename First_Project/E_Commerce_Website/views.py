from django.shortcuts import render
from django.http import HttpResponse
from . models import *

def Nav1(request):
    return render(request,"shop/main_Folder/main.html")
def form(request):
    return render(request,"form/index.html")
def collection(request):
    #category1=category.objects.filter()
    return render(request,"shop/collection.html")
     

# Create your views here.
