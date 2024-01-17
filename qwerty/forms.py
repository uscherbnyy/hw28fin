from django.forms import ModelForm, TextInput, Textarea, DateInput

from qwerty.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'description', 'assignee', 'due_date']
        widgets = {
            "task_name": TextInput(attrs={'placeholder': 'введите название задачи'}),
            "description": Textarea(attrs={'placeholder': 'введите описание'}),
            "due_date": DateInput(attrs={'placeholder': 'введите дату окончания'})
        }