from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def index(request):
    

    form = forms.CreateTodoForm() 
    context = {"form": form}      
    return render(request, "todos/index.html", context)

@require_http_methods(["POST"])
def action_add_new_todo(request):
    form = forms.CreateTodoForm(request.POST)
    instance = form.save()  
    return render(request, "todos/todo.html", {"item": instance})
