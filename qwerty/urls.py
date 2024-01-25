from django.urls import path

from qwerty import views


"""Настройте маршрутизацию (URL routing) в Django, чтобы пользователи могли получать доступ
 к каждому представлению (view) по правильному URL"""


urlpatterns = [
    path('', views.task_list, name='home'),
    path('task_create/', views.task_create),
    path('task_detail/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task_detail/<int:task_id>/reply_comment/<int:comment_id>', views.reply_comment, name='reply_comment'),
    path('logout/', views.logout_view, name='logout')

]