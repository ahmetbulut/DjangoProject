from django import forms

class AuthorForm(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)