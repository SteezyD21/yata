from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def index(request):
    return HttpResponse("Hello world")

    form = forms.CreateTodoForm() 
    context = {"form": form}      
    return render(request, "todos/index.html", context)