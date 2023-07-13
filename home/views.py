from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from home.models import Contact, Web

# Create your views here.
def home(request):
    #return HttpResponse("This is my Homepage")
   
    return render(request, 'home.html',)

def about(request):
    #return HttpResponse("This is my about page")
    return render(request, 'about.html')

def projects(request):
    #return HttpResponse("This is my projects page")
    return render(request, 'projects.html')

def web(request):
    if request.method=="POST":
        web= request.POST['web']
        link = request.POST['link']
        ins= Web (web=web,link=link)
        ins.save()
    return render(request, 'web.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        ins= Contact (name=name,email=email,phone=phone,desc=desc)
        ins.save()
        print('The Data has been written in the db')
    #return HttpResponse("This is my contact")
    return render(request, 'contact.html')
