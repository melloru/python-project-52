from django import forms


class BaseNameForm(forms.ModelForm):
    class Meta:
        fields = ["name"]
        widgets = {'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя", "maxlength": "100"})}
        labels = {'name': 'Имя'}

