from asyncio import tasks
from gettext import install
from django.shortcuts import redirect, render
from .models import MyTodo
from .forms import TodoForm
# Create your views here.


def allTodos(request):
    tasks = reversed(list(MyTodo.objects.all()))
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("all-todos")
    return render(request, 'allTodos.html', {"tasks": tasks, "form": form})


def deleteTodo(request, id):
    task = MyTodo.objects.get(id=id)
    task.delete()
    return redirect("all-todos")


def updateTodo(request, id):
    todo = MyTodo.objects.get(id=id)
    updateForm = TodoForm(instance=todo)
    if request.method == "POST":
        updateForm = TodoForm(request.POST, instance=todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect("all-todos")
    return render(request, 'updateTodo.html', {"todo": todo, "updateForm": updateForm})
