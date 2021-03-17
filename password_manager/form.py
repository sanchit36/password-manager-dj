from django import forms

from .models import Site


class AddSiteForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control mb-3", "placeholder": "Site Name", "autocomplete": "off"}))
    password = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control mb-3", "placeholder": "Site Password", "autocomplete": "off"}))

    class Meta:
        model = Site
        fields = ('name', 'password')
