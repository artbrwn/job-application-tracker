from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email")

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User


class CustomUserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")
        help_texts = {
            "username": "",
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].label = "Usuario"
        self.fields['email'].label = "Correo electrónico"

       