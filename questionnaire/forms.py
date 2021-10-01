from django import forms

# locale imports
from .models import Survey


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        exclude = []
        widgets = {
            'start_date': forms.DateTimeInput(
                attrs={
                    'placeholder': '2006-10-25 14:30:59',
                }
            ),
            'end_date': forms.DateTimeInput(
                attrs={
                    'placeholder': '2006-10-25 14:30:59',
                }
            ),
        }


class SurveyUpdateForm(forms.ModelForm):
    class Meta:
        model = Survey
        exclude = []
        widgets = {
            'start_date': forms.DateTimeInput(
                attrs={
                    'placeholder': '2006-10-25 14:30:59',
                }
            ),
            'end_date': forms.DateTimeInput(
                attrs={
                    'placeholder': '2006-10-25 14:30:59',
                }
            ),
        }
