from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from core.models import User


class LoginForm(AuthenticationForm):
    pass


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
