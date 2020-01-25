from django import forms
from . import models

EMPTY_LABEL = "--Select--"

class CompanyForm(forms.ModelForm):
    class Meta:
        model = models.Company
        fields = [
            'name',
        ]

class ConsoleForm(forms.ModelForm):
    company = forms.ModelChoiceField(
        queryset=models.Company.objects.order_by('name'),
        empty_label=EMPTY_LABEL,
    )

    class Meta:
        model = models.Console
        fields = [
            'company',
            'name',
        ]

class GameForm(forms.ModelForm):
    console = forms.ModelChoiceField(
        queryset=models.Console.objects.order_by('company__name', 'name'),
        empty_label=EMPTY_LABEL,
    )

    class Meta:
        model = models.Game
        fields = [
            'console',
            'title',
            'release_date',
        ]
        widgets = {
            'release_date': forms.TextInput(
                attrs={'placeholder': 'yyyy-mm-dd'}
            )
        }
