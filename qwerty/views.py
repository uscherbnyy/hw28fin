from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from qwerty.forms import TaskForm, CommentForm
from qwerty.models import Task, Comment

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


@login_required
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

"""Реализуйте функциональность добавления комментариев к задачам. Пользователи должны иметь возможность оставлять
 комментарии к задачам, обсуждать их и отвечать на комментарии других пользователей."""


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = task.comments.filter(parent__isnull=True)
    if request.method == 'POST':
        status = request.POST.get('status')

        if status in ['В процессе', 'Завершено']:
            task.status = status
            task.save()
            return redirect('task_detail', task_id=task_id)

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
            return redirect('task_detail', task_id=task_id)
    else:
        form = CommentForm()
    context = {
        'task': task,
        'comments': comments,
        'form': form,
    }
    return render(request, 'task_detail.html', context)


@login_required
def reply_comment(request, comment_id, task_id):
    task = get_object_or_404(Task, id=task_id)
    parent_comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.parent = parent_comment
            comment.save()
            return redirect('task_detail', task_id=task_id)
    else:
        form = CommentForm()
    context = {
        'task': task,
        'form': form,
        'parent_comment': parent_comment
    }
    return render(request, 'replay_comment.html', context)


"""Добавьте базовую аутентификацию, чтобы только зарегистрированные пользователи могли создавать задачи,
 назначать исполнителей, изменять статус выполнения и оставлять комментарии."""


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = '/profile.html/'


@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


def logout_view(request):
    logout(request)
    return redirect('home')
