from django.contrib import admin

# Register your models here.

from HauntedCheese.models import TodoIterator,Todo
admin.site.register(TodoIterator) 
admin.site.register(Todo)