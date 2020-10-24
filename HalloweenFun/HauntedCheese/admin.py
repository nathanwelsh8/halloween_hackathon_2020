from django.contrib import admin
from models import Todo, TodoIterator

# Register your models here.
admin.site.register(TodoIterator)
admin.site.register(Todo)