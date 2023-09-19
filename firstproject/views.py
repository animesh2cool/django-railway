from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import userForms
from service.models import Service

def homePage(request):
    serviceData=Service.objects().all()
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

def thankYou(request):
    if request.method =="GET":
        output=request.GET.get('output')
    return render(request,"thankyou.html",{'output':output})

def submitForm(request):
    return HttpResponse(request)

def userForm(request):
    finalans=0
    fn=userForms()
    data={'form':fn}
    try:
        if request.method=="POST":
         n1=int(request.POST.get('user'))
         n2=int(request.POST.get('password'))
        finalans=n1+n2
        print(finalans)
        data={
            'form':fn,
            'output':finalans
        }

        url="/thankyou/?output={}".format(finalans)

        return HttpResponseRedirect(url)

    except:
        pass
    return render(request,"userform.html",data)