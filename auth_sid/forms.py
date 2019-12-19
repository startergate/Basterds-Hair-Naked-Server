from django import forms

from auth_sid.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('pid', 'uid')
        app_label = 'auth_sid'
