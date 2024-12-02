from django.shortcuts import render, redirect
from .models import Task
from django.shortcuts import get_object_or_404


# View to list all tasks
def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

# View to add a new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST.get('due_date')  # Optional field
        Task.objects.create(title=title, description=description, due_date=due_date)
        return redirect('index')
    return render(request, 'tasks/add_task.html')


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST.get('due_date')
        task.status = request.POST['status']
        task.save()
        return redirect('index')
    return render(request, 'tasks/update_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'tasks/delete_task.html', {'task': task})


