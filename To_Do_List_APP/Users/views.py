from django.shortcuts import render,redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login/')
def AddTask(request):
    if request.method == 'POST':
        title = request.POST.get('task_title')
        description = request.POST.get('task')
        complete_by_date = request.POST.get('complete_by_date')
        # Create and save the new task
        Task.objects.create(user=request.user, title=title, description=description, complete_by_date=complete_by_date)
        return redirect('list_user_tasks')  # Redirect to the list view after adding
    return render(request, 'add_task.html', {'user': request.user})

@login_required(login_url='login/')
def EditTask(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('task_title')
        task.description = request.POST.get('task')
        task.complete_by_date = request.POST.get('complete_by_date')
        task.save()
        return redirect('list_user_tasks')
    return render(request, 'edit_task.html', {'task': task, 'user': request.user})

@login_required(login_url='login/')
def ListUserTasks(request):
    tasks = Task.objects.filter(user=request.user).order_by('complete_by_date') 
    return render(request, 'user_tasks.html', {'tasks': tasks, 'user': request.user})

@login_required(login_url='login/')
def DeleteTask(request, task_id):
    # Retrieve the task object by its ID, or return a 404 error if not found
    task =  get_object_or_404(Task, id=task_id)
    # Delete the task
    task.delete()
    # Redirect to the list of user tasks after deletion
    return redirect('list_user_tasks')