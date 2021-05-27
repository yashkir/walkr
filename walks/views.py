from typing import DefaultDict
from django.views import View
from .models import Walk, Stop, Picture
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse


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
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj


class WalkEdit(UpdateView):
    model = Walk
    template_name = 'walk_update_form.html'
    fields = ['title','description', 'is_public']

    def get_object(self):
        obj = Walk.objects.get(id=self.kwargs['pk'])
        return obj


class WalkDelete(DeleteView):
    model = Walk
    template_name = 'walk_confirm_delete.html'

    def get_object(self):
        obj = Walk.objects.get(id=self.kwargs['pk'])
        return obj

    def get_success_url(self):
        return reverse('walks_home')


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

    def get_context_data(self, **kwargs):
        obj = Stop.objects.get(id=self.kwargs['stop_id'])
        context = super().get_context_data(**kwargs)
        context['stop_title'] = obj.title
        context['walk_title'] = obj.walk.title
        context['stop_id'] = self.kwargs['stop_id']
        context['walk_id'] = self.kwargs['walk_id']
        return context

    def form_valid(self, form):
        form.instance.stop = Stop.objects.get(id=self.kwargs['stop_id'])
        return super().form_valid(form)


class StopCreate(CreateView):
    model = Stop
    template_name = "stop_form.html"
    fields = ['title','description', 'location_text', 'order']

    def form_valid(self, form):
        form.instance.walk = Walk.objects.get(id=self.kwargs['walk_id'])
        return super().form_valid(form)


class StopDetail(DetailView):
    model = Stop
    template_name = 'stop_detail.html'

    def get_object(self):
        obj = Stop.objects.get(id=self.kwargs['stop_id'])
        obj.stopsInWalk = Stop.objects.filter(walk_id=self.kwargs['walk_id']).order_by('created')
        obj.stopsInWalk.length = obj.stopsInWalk.count()
        key_no = 1
        dictionary_of_stops = {}
        for stop in obj.stopsInWalk:
            dictionary_of_stops[key_no] = stop
            if stop.id == self.kwargs['stop_id']:
                obj.currentStopNo=key_no
            key_no+=1
        #if the current stop is the first stop, set walk id and stop id of previous stop to -1
        if obj.currentStopNo == 1:
            obj.previous_stop_ID = -1
            obj.previous_walk_ID = -1
        else:
            obj.previous_stop_ID = dictionary_of_stops[obj.currentStopNo-1].id
            obj.previous_walk_ID = dictionary_of_stops[obj.currentStopNo-1].walk.id
        #if the current stop is the last stop, set walk id and stop id of next stop to -1
        if obj.currentStopNo == obj.stopsInWalk.length:
            obj.next_stop_ID = -1
            obj.next_walk_ID = -1
        else:
            obj.next_stop_ID = dictionary_of_stops[obj.currentStopNo+1].id
            obj.next_walk_ID = dictionary_of_stops[obj.currentStopNo+1].walk.id
        
        obj.last_accessed = timezone.now()
        obj.save()
        return obj


class StopEdit(UpdateView):
    model = Stop
    template_name = 'stop_update_form.html'
    fields = ['title','description', 'location_text', 'order']

    def get_object(self):
        obj = Stop.objects.get(id=self.kwargs['stop_id'])
        return obj


class StopDelete(DeleteView):
    model = Stop
    template_name = 'stop_confirm_delete.html'

    def get_object(self):
        obj = Stop.objects.get(id=self.kwargs['stop_id'])
        return obj

    def get_success_url(self):
        return reverse('walk_detail', kwargs={ 'pk': self.kwargs['walk_id'] })
