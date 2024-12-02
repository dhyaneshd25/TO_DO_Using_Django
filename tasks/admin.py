from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'due_date', 'status')
    list_filter = ('status', 'timestamp')
    search_fields = ('title',)
