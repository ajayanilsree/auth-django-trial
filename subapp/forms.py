from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

        for field_name, field in self.fields.items():
            field.label = ''                 # ✅ remove label
            field.help_text = None           # ✅ remove help text
            field.widget.attrs['placeholder'] = placeholders.get(field_name, '')

class LoginForm(AuthenticationForm):
    pass