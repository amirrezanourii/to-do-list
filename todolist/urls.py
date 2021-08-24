from django.contrib import admin
from django.urls import path, include
from todo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', views.index, name='todo'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('delete/<int:task_id>', views.remove, name='remove'),
]
