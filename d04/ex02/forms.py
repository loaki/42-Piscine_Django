from django import forms


class History(forms.Form):
    history = forms.CharField(label='history')
    jules = forms.CharField(label='jules')
