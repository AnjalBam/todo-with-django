from django.shortcuts import render
from django.http import HttpResponseRedirect


from django.utils import timezone
from todo.models import Todo

# Create your views here.

def home_view(request):
    todo_items = Todo.objects.all().order_by('-added_date')

    context = {
        'todo_items': todo_items
    }

    return render(request, 'todo/index.html', context)


def add_todo_view(request):
    # print(request.POST.get(todo))

    date_now = timezone.now()
    todo = request.POST['todo']
    add_todo(todo, date_now)
 
    return HttpResponseRedirect('/')



def add_todo(todo, date_now):
    if todo == '' or None:
        return
    else:
        Todo.objects.create(text=todo, added_date=date_now)


def delete_todo_view(request, todo_id):
    # print(request.POST.get(todo))
    Todo.objects.get(id=todo_id).delete()
    

    return HttpResponseRedirect('/')
