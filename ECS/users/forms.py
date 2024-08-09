from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from django.contrib.auth import get_user_model

class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','password1','password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.save()
        return user

class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','password']
