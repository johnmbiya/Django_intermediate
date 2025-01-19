from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'role']
        labels = {
            'username': 'Nom d\'utilisateur',
            'email': 'Adresse email',
        }
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None
        }
        error_messages = {
            'username': {
                'unique': 'Ce nom d\'utilisateur est déjà pris.'
            },
            'email': {
                'unique': 'Cette adresse email est déjà utilisée.'
            }
        }