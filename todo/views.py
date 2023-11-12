from django.shortcuts import render
from django.views.generic.list import ListView
from .models import TodoModel

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel