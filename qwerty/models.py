from django.db import models

# Create your models here.
from django.db import models


"""Создайте модели Task и User"""


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class Task(models.Model):
    STATUS_CHOICES = (
        ('В ожидании', 'В ожидании'),
        ('В процессе', 'В процессе'),
        ('Завершено', 'Завершено')
    )

    task_name = models.CharField(max_length=200)
    description = models.TextField()
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name = "задача"
        verbose_name_plural = "задачи"


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
