from django.http import HttpResponse
from django.shortcuts import render, redirect

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