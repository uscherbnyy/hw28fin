from django.contrib import admin

# Register your models here.

from qwerty.models import User, Task, Comment

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Comment)