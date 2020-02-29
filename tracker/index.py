from django import forms

class Tracker(forms.Form):
    date          = forms.CharField(max_length=120)
    issue         = forms.CharField(max_length=120)
    description   = forms.CharField(max_length=120)
    severity      = forms.CharField(max_length=120)
    reporter      = forms.CharField(max_length=120)
    owner         = forms.CharField(max_length=120)
    status        = forms.CharField(max_length=120)
    comments      = forms.CharField(max_length=120)
    occ           = forms.CharField(max_length=120)
