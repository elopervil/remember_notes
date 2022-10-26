from django import forms
from .models import Notes


class AddNotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = [
            'title',
            'description',
            'done_date'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'Placeholder': 'Nombre'}),
            'description': forms.Textarea(attrs={'Placeholder': 'Descripcion'}),
            'done_date': forms.DateTimeInput(attrs={'type': 'date'})
        }
        labels = {
            'title': 'Nombre',
            'description': 'Descripcion',
            'done_date': 'Fecha limite'
        }
