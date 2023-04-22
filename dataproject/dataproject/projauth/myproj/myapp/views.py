from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# Create your views here.


def home(request):
    return render(request,"myapp/home.html")


@login_required(login_url='accounts/login')
def Students(request):
    return render(request,"myapp/students.html")


@permission_required('myapp.view_labs')
def lab(request):
    return render(request, "myapp/labs.html")