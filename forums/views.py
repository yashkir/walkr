from django.views import View
from django.views.generic import ListView, DetailView

from .models import Forum, Thread, Post


class ForumList(ListView):
    model = Forum


class ForumDetail(DetailView):
    model = Forum
