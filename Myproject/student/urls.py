
from django.urls import path,include
from . import views
urlpatterns = [

    path('student-list/',views.Dispaly, name="student_list"),
    
]
