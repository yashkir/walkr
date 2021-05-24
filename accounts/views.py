from django.urls import reverse_lazy

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


class Profile(TemplateView):
    template_name = 'accounts/profile.html'

class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
