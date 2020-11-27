from django.shortcuts import render

# Create your views here.

def home(request):
    context={
        'home_active':'active',
        'home_disabled':'disabled',
        }
    return render(request,'core/home.html',context)