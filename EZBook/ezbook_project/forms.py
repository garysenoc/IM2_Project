from django import forms
from ezbook_project.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'firstname',
            'middlename',
            'lastname',
            'age',
            'phone_number',
            'email',
        )
