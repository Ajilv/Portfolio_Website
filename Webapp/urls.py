from django.urls import path
from Webapp import views
urlpatterns=[
    path('',views.HomePage,name="HomePage"),
    path('Project/',views.Project,name="Project"),
    path('save_contact/',views.save_contact,name="save_contact")
]