from django import forms
from django.contrib.auth.forms import UserCreationForm

from guests.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Tylko poprawny adres email.',
    )
    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ('email', 'phone', 'password1', 'password2')