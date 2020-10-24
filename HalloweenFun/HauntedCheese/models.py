from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

PENDING = 0
DONE = 1

COMPLETE_STATUS = (
    (PENDING, 'Pending'),
    (DONE, 'Done'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# Todo List Model
class Todo(models.Model):
    user = models.ForeignKey(UserProfile,default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_time = models.DateTimeField(default=timezone.now)
    due_time = models.DateTimeField(default=timezone.now)
    status = models.PositiveSmallIntegerField(choices=COMPLETE_STATUS)

    class Meta:
        ordering = ["-created_time"]
    
    def __str__(self):
        return self.title