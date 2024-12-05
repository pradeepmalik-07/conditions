from django.shortcuts import render

# Create your views here.

def condi(request):
    d={'name':'pradeep','age':28}
    return render(request,'conditions.html',d)