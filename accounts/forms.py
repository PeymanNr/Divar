from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import MyUser, Profile


class RegisterForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('phone_number',)


class LoginFrom(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('phone_number',)


class SearchForm(forms.Form):
    search = forms.CharField()


class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'joined_at', 'my_city')
