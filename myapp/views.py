from django.shortcuts import render
from myapp.models import Task
# Create your views here.

from django.http import HttpResponseRedirect


def index(request):
    tasks = Task.objects.all()
    tasks = {'all_tasks': tasks}
    return render(request, 'Home/index.html', tasks)


def Add_todo(request):
    # create a new todo item
    titl = request.POST['title']
    descr = request.POST['description']
    comp = request.POST['is_completed']
    time = request.POST['time']
    new_item = Task(title=titl, description=descr,
                    is_completed=comp, time=time)
    # save
    new_item.save()
    # redirect the browser to '/'
    return HttpResponseRedirect('/')


def delete_item(request, todo_id):
    # find the item by id
    item_to_del = Task.objects.get(id=todo_id)
    print('todo id = ', todo_id)
    print('item to del = ', item_to_del)
    item_to_del.delete()
    return HttpResponseRedirect('/')


def item_desc(request, todo_id):
    item = Task.objects.get(id=todo_id)
    item_details = {'item': item}
    return render(request, 'Home/result.html', item_details)

def search(request):
    items = []
    query = request.POST['search']
    if len(query) > 51:
        items= None
        searched_items = {'item': items,'query':query}
        return render(request, 'Home/search.html', searched_items)
    else:
        items_filt_title = Task.objects.filter(title__icontains=query)
        items_filt_desc = Task.objects.filter(description__icontains=query)
        final_set= items_filt_title.union(items_filt_desc)
        searched_items = {'item': final_set,'query':query}
        return render(request, 'Home/search.html', searched_items)
