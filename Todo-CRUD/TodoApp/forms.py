from django import forms
from .models import Todo


# Creating a form
class TodoForm(forms.ModelForm):
    # meta class
    class Meta:
        # model to be used
        model = Todo
        fields = [
            'title',
            'description'
        ]
