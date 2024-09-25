from django.urls import path
from . import views


urlpatterns = [
    path('add-task/', views.AddTask, name='add_task'),
    path('edit-task/<int:task_id>/', views.EditTask, name='edit_task'),
    path('user-tasks/', views.ListUserTasks, name='list_user_tasks'),
    path('delete-tasks/<int:task_id>/', views.DeleteTask, name='delete_task'),
]

