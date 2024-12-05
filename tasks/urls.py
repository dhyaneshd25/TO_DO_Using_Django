from django.urls import path
from tasks import views  # Import views from the tasks app

urlpatterns = [
    path('', views.index, name='index'),         # Homepage
    path('add/', views.add_task, name='add_task'),  # Add Task
     path('update/<int:task_id>/', views.update_task, name='update_task'),  # Update Task
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete Task
]
