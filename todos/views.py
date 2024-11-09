from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models

# Create your views here.

@require_http_methods(["GET"])
def index(request):
    form = forms.CreateTodoForm()
    todos = models.TodoItem.objects.all() 
    context = {"todo_items": todos, "form": form} 
    return render(request, "todos/index.html", context)

@require_http_methods(["POST"])
def action_add_new_todo(request):
    form = forms.CreateTodoForm(request.POST)
    instance = form.save()  
    return render(request, "todos/todo.html", {"item": instance})
