from django.db import models

# Create your models here.


class SkillDb(models.Model):
    name=models.CharField(max_length=60,null=True,blank=True)


class ProjectDb(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    desc = models.TextField(max_length=250, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    img1 = models.ImageField(upload_to="projects/", null=True, blank=True)
    img2 = models.ImageField(upload_to="projects/", null=True, blank=True)
    img3 = models.ImageField(upload_to="projects/", null=True, blank=True)
    skills = models.TextField(max_length=200,null=True, blank=True)