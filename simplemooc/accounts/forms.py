from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def dict_from_class(cls):
     return dict(
         (key, value)
         for (key, value) in cls.__dict__.items()
         if key not in _excluded_keys
         )

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe Usuário com Este E-mail')
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)

        user.email = self.cleaned_data['email']


        if commit:
            user.save()
        return user
