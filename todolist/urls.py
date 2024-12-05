from django.contrib import admin
from django.urls import path, include  # Use include for app URLs

urlpatterns = [
    path('to-do-using-django-git-main-dhyanesh-dharmiks-projects.vercel.app/', admin.site.urls),
    path('', include('tasks.urls')),  # Include URLs from the tasks app
]
