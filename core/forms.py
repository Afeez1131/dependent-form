from django import forms

from core.models import Person, Town


class CreatePersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'state', 'town']