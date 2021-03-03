from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import WalletUser


class WalletUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = WalletUser
        fields = ('phone_number',)


class WalletUserChangeForm(UserChangeForm):

    class Meta:
        model = WalletUser
        fields = ('phone_number',)