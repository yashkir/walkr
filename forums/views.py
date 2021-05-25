from django.views import View
from django.views.generic import ListView

from .models import Forum, Thread, Post


class ForumsList(ListView):
    model = Forum
