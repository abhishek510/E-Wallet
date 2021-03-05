from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required

from .forms import WalletUserCreationForm


class SignUp(generic.CreateView):
    form_class = WalletUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'