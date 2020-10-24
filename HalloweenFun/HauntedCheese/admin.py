from django.contrib import admin
from .models import UserProfile, TodoIterator, Todo

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(TodoIterator)
admin.site.register(Todo)