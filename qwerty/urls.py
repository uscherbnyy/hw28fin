from django.urls import path

from qwerty import views

urlpatterns = [
    path('', views.task_list),
    path('task_create/', views.task_create),
    path('task_detail/<int:task_id>/', views.task_detail, name='task_detail'),

]