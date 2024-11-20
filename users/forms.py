from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'email',
            'last_name',
            'first_name',
            'middle_name',
            'username',
            'gender',
            'date_of_birthday',
        )
