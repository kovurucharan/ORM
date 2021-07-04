from django.shortcuts import render
from WebApp.models import Team

def TeamView(request):
    items=Team.objects.all()
    return render(request,'MyApp/Welcome.html',{'items':items})
