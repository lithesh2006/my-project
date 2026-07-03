from django.shortcuts import render

# Create your views here.
def Dispaly(request):
    return render(request,'student-list.html')