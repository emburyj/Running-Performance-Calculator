from django import forms

class time_input_form(forms.Form):
    seconds = forms.IntegerField(label="sec", min_value=0, max_value=59, required=False)
    minutes = forms.IntegerField(label="min", min_value=0, max_value=59, required=False)
    hours = forms.IntegerField(label="hr", min_value=0, required=False)

