from django.shortcuts import render
from random import randint


from .models import student

def fun1(request):
    return render(request,'display.html')


def fun2(request):
    if request.method=="POST":
        a=request.POST['us']
        b=request.POST['pa']
        c=randint(145662,558963)
        sd=student(name=a,password=b,id=c)
        sd.save()
    return render(request,'display.html')


