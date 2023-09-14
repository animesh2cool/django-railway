from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title': 'Home page',
        'body': 'created by @nimesh',
        'clist': ['Java','Python','js'],
        'student_details': [
            {'name':'animesh', 'phone':'7003440120'},
            {'name':'ranu', 'phone':'980012345'},
            {'name':'sagir', 'phone':'55988612'}
        ]
    }
    return render(request,"index.html",data)

def aboutPage(request):
    return HttpResponse("Welcome  to the about page")

def courses(request):
    return HttpResponse("B. Tech /n M. Tech.")

def courseDetails(request,courseid):
    return HttpResponse(courseid)