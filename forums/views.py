from django.views import View
from django.views.generic import ListView, DetailView

from .models import Forum, Thread, Post


class ForumsList(ListView):
    model = Forum


class ForumsDetail(DetailView):
    model = Forum
