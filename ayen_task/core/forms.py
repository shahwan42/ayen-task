from django import forms
from ayen_task.core.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ("name", "file")
