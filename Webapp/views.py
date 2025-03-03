from django.shortcuts import render,redirect
from InfoApp.models import ProjectDb
from Webapp.models import ContactDb
# Create your views here.
def HomePage(request):
    return render(request,"Home.html")
def Project(request):
    projects=ProjectDb.objects.all()
    return render(request,"Project.html",{'projects':projects})

def save_contact(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        mess=request.POST.get('message')
        obj1=ContactDb(name=na,email=em,message=mess)
        obj1.save()
        return redirect(HomePage)
