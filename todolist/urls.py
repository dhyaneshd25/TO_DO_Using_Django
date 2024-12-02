from django.contrib import admin
from django.urls import path, include  # Use include for app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Include URLs from the tasks app
]
