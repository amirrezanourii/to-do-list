from django.contrib import admin
from .models import ToDoList


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    # list_filter = ('status',)
    ordering = ('created',)
