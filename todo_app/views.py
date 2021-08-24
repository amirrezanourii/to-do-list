from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import ToDoList
from .forms import ToDoForm


def index(request):
    item_list = ToDoList.objects.order_by('-created')

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = ToDoForm()

    return render(request, "todo_app/index.html", {'form': form,
                                                   'item_list': item_list})

@csrf_exempt
def remove(request, task_id):
    item = ToDoList.objects.get(id=task_id)
    item.delete()
    return redirect('todo')

