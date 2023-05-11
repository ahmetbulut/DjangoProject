from django import forms
from library.models import Publisher

class AuthorForm(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    #date = forms.DateField(widget=forms.SelectDateWidget)

class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    numpages = forms.IntegerField(widget=forms.NumberInput)
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all())