from django.shortcuts import render
from myapp.models import Task
# Create your views here.

from django.http import HttpResponseRedirect

def index(request):
	tasks= Task.objects.all()
	tasks={'all_tasks':tasks}
	return render(request, 'Home/index.html',tasks)		

def desc(request):
	# create a new todo item
	titl= request.POST['title']
	descr= request.POST['description']
	comp= request.POST['is_completed']
	new_item= Task(title=titl,description=descr,is_completed=comp)
	# save
	new_item.save()
	# redirect the browser to '/'
	return HttpResponseRedirect('/')


















