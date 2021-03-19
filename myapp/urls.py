from django.urls import path
from . import views

urlpatterns= [
	path('',views.index,name='main'),
	path('Add_todo/',views.Add_todo),
	path('del/<int:todo_id>/', views.delete_item),
	path('desc/<int:todo_id>/', views.item_desc),
]