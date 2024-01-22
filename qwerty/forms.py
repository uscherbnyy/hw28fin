from django.forms import ModelForm, TextInput, Textarea, DateInput, ModelChoiceField

from qwerty.models import Task, User


class TaskForm(ModelForm):
    assignee = ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['task_name', 'description', 'assignee', 'due_date']
        widgets = {
            "task_name": TextInput(attrs={'placeholder': 'введите название задачи'}),
            "description": Textarea(attrs={'placeholder': 'введите описание'}),
            "due_date": DateInput(attrs={'placeholder': 'введите дату окончания'})
        }
