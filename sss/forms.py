import django.forms.widgets
from django.forms import ModelForm, Textarea, TextInput, ChoiceField
from sss.models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={"size": 20}),
        }