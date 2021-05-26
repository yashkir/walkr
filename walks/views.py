from django.views import View
from .models import Walk, Stop, Picture
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.utils import timezone


class WalkCreate(CreateView):
    template_name="walk_form.html"
    model = Walk
    fields = ['title', 'description', 'is_public']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WalkDetail(DetailView):
    # breakpoint()
    model = Walk
    template_name = 'walk_detail.html'

    def get_object(self):
        print(f"self----> {self}")
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj


class WalksList(ListView):
    model = Walk
    template_name = 'walk_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PictureCreate(CreateView):
    model = Picture
    template_name = 'add_picture.html'
    fields = ['title', 'image']

class StopCreate(CreateView):
    model = Stop
    template_name = "stop_form.html"
    fields = ['title','description', 'location_text', 'order']

    def form_valid(self, form):
        form.instance.walk = Walk.objects.get(id=self.kwargs['walk_id'])
        # form.instance.order = self.request.user
        return super().form_valid(form)