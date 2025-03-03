from django.shortcuts import render,redirect
from InfoApp.models import SkillDb,ProjectDb

from django.contrib import messages
from datetime import datetime


# Create your views here.
def Index_page(request):
    return render(request,"index.html")

def Add_Projects(request):
    data1=SkillDb.objects.all()
    return render(request,"Add_Projects.html",{'data1':data1})



from django.shortcuts import render, redirect
from .models import ProjectDb

def save_project(request):
    if request.method == "POST":
        name = request.POST.get("name")
        skills = request.POST.getlist("skills")  # Get selected skills as a list
        desc = request.POST.get("desc")
        date = request.POST.get("date")

        img1 = request.FILES.get("img1")
        img2 = request.FILES.get("img2")
        img3 = request.FILES.get("img3")

        # If no skills are selected, set a default value (e.g., "No skills selected")
        skills_str = ", ".join(skills) if skills else "No skills selected"

        # Save project to database
        project = ProjectDb(
            name=name,
            skills=skills_str,  # Save as a comma-separated string
            desc=desc,
            date=date,
            img1=img1,
            img2=img2,
            img3=img3
        )
        project.save()

        return redirect("View_Projects")  # Redirect to the project list page


def View_Projects(request):
    projects = ProjectDb.objects.all()
    return render(request,"View_Projects.html",{'projects':projects})

def Delete_project(request,pid):
    data=ProjectDb.objects.get(id=pid)
    data.delete()
    return redirect(View_Projects)






def Add_Skill(request):
    return render(request,"Add_Skill.html")

def Save_Skills(request):
    if request.method=="POST":
        na=request.POST.get('name')
        obj1=SkillDb(name=na)
        obj1.save()
        return redirect(View_Skills)

def View_Skills(request):
    data=SkillDb.objects.all()
    return render(request,"View_Skills.html",{'data':data})

def Del_Skills(request,sid):
    obj=SkillDb.objects.get(id=sid)
    obj.delete()
    return redirect(View_Skills)