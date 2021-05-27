from typing import DefaultDict
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
        print(f"self----> {self}")
        # breakpoint()
        obj = Stop.objects.get(id=self.kwargs['stop_id'])
        obj.stopsInWalk = Stop.objects.filter(walk_id=self.kwargs['walk_id']).order_by('created')
        obj.stopsInWalk.length = obj.stopsInWalk.count()
        key_no = 1
        dictionary_of_stops = {}
        for stop in obj.stopsInWalk:
            dictionary_of_stops[key_no] = stop
            print('stop')
            print(stop.location_text)
            print(stop.id)
            if stop.id == self.kwargs['stop_id']:
                obj.currentStopNo=key_no
                print(obj.currentStopNo)
            else:
                print("FALSE")
            key_no+=1
        print(dictionary_of_stops)
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