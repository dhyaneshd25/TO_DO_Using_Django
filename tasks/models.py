from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('OPEN', 'Open'),
            ('WORKING', 'Working'),
            ('PENDING_REVIEW', 'Pending Review'),
            ('COMPLETED', 'Completed'),
            ('OVERDUE', 'Overdue'),
            ('CANCELLED', 'Cancelled'),
        ],
        default='OPEN',
    )

    def __str__(self):
        return self.title

