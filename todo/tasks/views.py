
from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks=Task.objects.all().order_by("-id")
    return render(request,"tasks/index.html",{
        "tasks":tasks
    })

def create_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        
        if form.is_valid():
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            is_completed=form.cleaned_data['is_completed']

            form.save()
            return redirect('index')

    else:
            form=TaskForm()
    
    return render(request,"tasks/create_task.html",{
        "form":form
    })

def delete_task(request,id):
     task=Task.objects.get(id=id)
     if request.method=="POST":
          task.delete()

          return redirect('index')
     return render(request,"tasks/delete_task.html",{
          "task":task
        })

def edit_task(request,id):
    task=Task.objects.get(id=id)

    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
         form=TaskForm(instance=task)

    return render(request,"tasks/edit_task.html",{
         "form":form
    })



