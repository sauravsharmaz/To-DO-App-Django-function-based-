from django.shortcuts import render
from myapp.models import Task
# Create your views here.

from django.http import HttpResponse

def index(request):
	tasks= Task.objects.all()
	tasks={'all_tasks':tasks}
	return render(request, 'Home/index.html',tasks)		

def desc(request):
	tasks= Task.objects.all()
	tasks={'all_tasks':tasks}
	return render(request,'Home/result.html',tasks)



















