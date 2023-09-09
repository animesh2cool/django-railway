from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def aboutPage(request):
    return HttpResponse("Welcome  to the about page")

def courses(request):
    return HttpResponse("B. Tech /n M. Tech.")

def courseDetails(request,courseid):
    return HttpResponse(courseid)