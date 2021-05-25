from django.views import View
from .models import Walk, Stop, Picture
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone

# Placeholder
class Home(View):
    def get(self, request):
        from django.http import HttpResponse
        return HttpResponse('<h1>Hit walks/ path</h1>')

class allWalks(View):
    model=Walk
    
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
    print('BEEP BOOP')
    # print(queryset)
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
    #wHAT DOES this do????????
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class StopCreate(CreateView):
    template_name = "add_stop_form.html"
    model = Stop
    fields = ['title','description', 'is_public']