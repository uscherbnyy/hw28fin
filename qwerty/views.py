from django.http import HttpResponse
from django.shortcuts import render

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
