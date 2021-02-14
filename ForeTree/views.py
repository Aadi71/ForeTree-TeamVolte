from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'About.html')
def mission(request):
    return render(request,'mission.html')
def contact(request):
    return render(request,'contact.html')
def solutions(request):
    return render(request,'QnA.html')