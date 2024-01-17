from django.urls import path

from qwerty import views

urlpatterns = [
    path('', views.home),

]