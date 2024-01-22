from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from qwerty.forms import TaskForm
from qwerty.models import Task

# Create your views here.


"""
Создайте представление (view) для отображения списка всех задач на главной странице. Задачи должны быть отсортированы 
по дате создания в обратном порядке (самые новые задачи должны быть вверху).
"""


def task_list(request):
    tasks = Task.objects.order_by('-created_date')
    context = {
        'tasks': tasks,
    }
    return render(request, 'task_list.html', context)


"""Создайте представление (view) для создания новой задачи. На странице создания задачи пользователь должен ввести
 название, описание, исполнителя и дату завершения задачи."""


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'task_create.html', context)


"""Создайте представление (view) для просмотра отдельной задачи. Пользователи должны иметь возможность просматривать
 детали задачи, включая описание, исполнителя, статус выполнения и комментарии к задаче"""

"""Реализуйте функциональность обновления статуса выполнения задачи. Пользователи должны иметь возможность изменять
 статус выполнения задачи на "В процессе" и "Завершено".
"""


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        status = request.POST.get('status')

        if status in ['В процессе', 'Завершено']:
            task.status = status
            task.save()
            return redirect('task_detail', task_id=task_id)

    context = {
        'task': task,
    }
    return render(request, 'task_detail.html', context)


