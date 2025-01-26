from django import forms

class ChirpForm(forms.Form):
    message = forms.Textarea(label = "message", max_length=255)