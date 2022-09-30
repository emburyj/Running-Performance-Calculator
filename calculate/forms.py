from django import forms

class time_input_form(forms.Form):
    hours = forms.IntegerField(label="hr", min_value=0, required=False, initial=0, widget=forms.NumberInput(attrs={'class': 'narrow-field'}))
    minutes = forms.IntegerField(label="min", min_value=0, max_value=59, required=False, initial=0, widget=forms.NumberInput(attrs={'class': 'narrow-field'}))
    seconds = forms.IntegerField(label="sec", min_value=0, max_value=59, required=False, initial=0, widget=forms.NumberInput(attrs={'class': 'narrow-field'}))

unit_choices = ((1, 'Miles'), (1, 'Kilometers'))

class target_race_form(forms.Form):
    distance = forms.DecimalField(min_value=0, initial=1)
    units = forms.ChoiceField(label = "", choices=unit_choices, required=False)
    avg_grade = distance = forms.DecimalField(min_value=0, max_value=100, decimal_places=1, initial=0, required=False)