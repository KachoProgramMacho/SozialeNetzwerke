from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, loader,RequestContext
from django.template import RequestContext
from .models import Todo
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def index(request):
    allTodos = Todo.objects.all()
    template = loader.get_template("Homepage.html")
    context = {
        'allTodos' : allTodos,
    }
    return HttpResponse(template.render(context,request))
@csrf_exempt
def create(request):
    if request.method == "POST":
        my_model = Todo()
        my_model.percent = request.POST.get("percent", "")
        my_model.description = request.POST.get("description", "")
        my_model.deadline = request.POST.get("deadline", "")
        my_model.save()
        return redirect("/")
    else:
        return HttpResponse(render_to_response("CreateTODO.html"))
@csrf_exempt
def delete(request,pk):
    toBeDeleted = Todo.objects.get(pk=pk)
    toBeDeleted.delete()
    return redirect('/')
def impressum(request):
    return HttpResponse(render_to_response("Impressum.html"))
@csrf_exempt
def edit(request,pk):
    if request.method == "POST":
        toBeEdited = Todo.objects.get(pk=pk)
        toBeEdited.percent = request.POST.get("percent", "")
        toBeEdited.description = request.POST.get("description", "")
        toBeEdited.deadline = request.POST.get("deadline", "")
        toBeEdited.save()
        return redirect('/')
    else:
        currentTodo = Todo.objects.get(id=pk)
        return render(request,"EditTODO.html",{"currentTodo":currentTodo})

