from django.urls import reverse_lazy

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
