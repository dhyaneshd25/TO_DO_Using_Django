from django.shortcuts import render, redirect
from .models import Task
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date


# View to list all tasks
def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

# View to add a new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        # Validate the due_date field
        due_date = request.POST.get('due_date')
        if due_date:
            parsed_date = parse_date(due_date)
            if parsed_date is None:
                raise ValidationError("Invalid date format. It must be in YYYY-MM-DD format.")
            # Valid date, set it
            task_due_date = parsed_date
        else:
            task_due_date = None  # If no due date is provided, set it to None

        # Create the new task
        Task.objects.create(
            title=title,
            description=description,
            due_date=task_due_date
        )
        return redirect('index')
    return render(request, 'tasks/add_task.html')


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']

        # Validate the due_date field
        due_date = request.POST.get('due_date')
        if due_date:
            parsed_date = parse_date(due_date)
            if parsed_date is None:
                raise ValidationError("Invalid date format. It must be in YYYY-MM-DD format.")
            task.due_date = parsed_date
        else:
            task.due_date = None  # If no date is provided, set it to None

        task.save()
        return redirect('index')
    return render(request, 'tasks/update_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'tasks/delete_task.html', {'task': task})


