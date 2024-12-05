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
        # Safely get POST data using get(), not directly accessing with ['key']
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Check if required fields are present
        if not title or not description:
            return render(request, 'tasks/add_task.html', {'error': 'Title and description are required.'})

        # Validate the due_date field if provided
        due_date = request.POST.get('due_date')
        task_due_date = None  # Default to None if no due date is provided
        if due_date:
            parsed_date = parse_date(due_date)
            if parsed_date is None:
                # If date parsing fails, raise a validation error
                return render(request, 'tasks/add_task.html', {'error': 'Invalid date format. It must be in YYYY-MM-DD format.'})
            task_due_date = parsed_date

        # Create the new task
        Task.objects.create(
            title=title,
            description=description,
            due_date=task_due_date
        )

        return redirect('index')  # Redirect to the homepage after adding the task

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


