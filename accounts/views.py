from django.shortcuts import render
from django.http import HttpResponse
def lead(request):
    return render(request,"lead.html")

# Create your views here.
