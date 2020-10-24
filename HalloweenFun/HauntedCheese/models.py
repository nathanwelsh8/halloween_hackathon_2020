from django.db import models
from datetime import timezone

PENDING = 0
DONE = 1

COMPLETE_STATUS = (
    (PENDING, 'Pending'),
    (DONE, 'Done')
)

class TodoIterator(models.Model):
    list_names = models.CharField(max_length=255)

# Todo List Model
class Todo(models.Model):
    list_title = models.ForeignKey(TodoIterator, on_delete=models.CASCADE)
    list_content = models.TextField(blank=True)
    created_time = models.DateTimeField(default=timezone.now())
    due_time = models.DateTimeField(default=timezone.now())
    status = models.PositiveSmallIntegerField(choices=COMPLETE_STATUS)

    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return self.list_title