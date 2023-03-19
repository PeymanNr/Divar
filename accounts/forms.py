from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import UpdateView

from accounts.models import MyUser, Profile


class RegisterForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('phone_number', 'nickname')


class LoginFrom(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('phone_number',)


class SearchForm(forms.Form):
    search = forms.CharField()


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['nickname']


class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = ('user', 'nickname', 'joined_at')