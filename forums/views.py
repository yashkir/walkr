from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView

from .models import Forum, Thread, Post


class ForumList(ListView):
    model = Forum


class ForumDetail(DetailView):
    model = Forum


class ThreadDetail(DetailView):
    model = Thread


class ThreadCreate(CreateView):
    model = Thread
    fields = ['title']

    def form_valid(self, form):
        form.instance.forum_id = self.kwargs['forum_id']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forum'] = Forum.objects.get(id=self.kwargs['forum_id'])
        return context

    def get_success_url(self):
        return reverse('threads_detail', kwargs={ 'pk': self.object.id })


class PostCreate(CreateView):
    model = Post
    fields = ['text']

    def form_valid(self, form):
        thread = Thread.objects.get(id=self.kwargs['thread_id'])
        thread.post_count = thread.post_count + 1
        thread.save()

        form.instance.author = self.request.user
        form.instance.position = thread.post_count
        form.instance.thread_id = self.kwargs['thread_id']

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thread'] = Thread.objects.get(id=self.kwargs['thread_id'])
        return context

    def get_success_url(self):
        return reverse('threads_detail', kwargs={ 'pk': self.kwargs['thread_id'] })

class PostDelete(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('threads_detail', kwargs={ 'pk': self.object.thread.id })
