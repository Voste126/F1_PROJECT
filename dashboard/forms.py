# dashboard/forms.py

from django import forms

class RaceDataForm(forms.Form):
    year = forms.IntegerField(label="Year", initial=2021)
    event = forms.CharField(label="Event Name", max_length=100, initial="Italian Grand Prix")
    
    SESSION_TYPE_CHOICES = [
        ('R', 'Race'),
        ('Q', 'Qualifying'),
        ('FP', 'Free Practice'),
    ]
    session_type = forms.ChoiceField(label="Session Type", choices=SESSION_TYPE_CHOICES)
