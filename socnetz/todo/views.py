from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import Context, loader
from django.template import RequestContext
from .models import Todo


# Create your views here.
def index(request):
    allTodos = Todo.objects.all()
    template = loader.get_template("Homepage.html")
    context = {
        'allTodos' : allTodos,
    }
    return HttpResponse(template.render(context,request))
def create(request):
    return HttpResponse(render_to_response("CreateTODO.html"))
