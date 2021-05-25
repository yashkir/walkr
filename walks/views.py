from django.views import View
from .models import Walk, Stop, Picture
from walks.forms import CreateWalkForm
from django.views.generic.edit import FormView


# Placeholder
class Home(View):
    def get(self, request):
        from django.http import HttpResponse
        return HttpResponse('<h1>Hit walks/ path</h1>')

from django import forms

class CreateWalkFormView(FormView):
    template_name = 'create_walk.html'
    form_class = CreateWalkForm
    success_url = '/success/'
    message = forms.CharField(widget=forms.Textarea)

    def form_valid(self, form):
        return super().form_valid(form)