from django.urls import path
from InfoApp import views
urlpatterns=[
    path('Index_page/',views.Index_page,name="Index_page"),
    path('Add_Projects/',views.Add_Projects,name="Add_Projects"),
    path('View_Projects/',views.View_Projects,name="View_Projects"),
    path('save_project/',views.save_project,name="save_project"),
    path('Delete_project/<int:pid>',views.Delete_project,name="Delete_project"),




    path('Add_Skill/',views.Add_Skill,name="Add_Skill"),
    path('View_Skills/',views.View_Skills,name="View_Skills"),
    path('Save_Skills/',views.Save_Skills,name="Save_Skills"),
    path('Del_Skills/<int:sid>',views.Del_Skills,name="Del_Skills"),

    path('ViewContact',views.contactInfo,name="Contact_details"),
    path('Del_contact/<int:cid>',views.Del_contact,name="Del_contact")
]