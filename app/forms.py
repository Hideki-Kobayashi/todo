from django import forms
from .models import Contribution
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ("theme", "deadline", "memo")

        
        
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
            
class SearchForm(forms.Form):
    keyword = forms.CharField(min_length = 2, max_length = 100, label="")