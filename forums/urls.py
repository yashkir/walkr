from django.urls import path

from . import views

urlpatterns = [
    path('', views.ForumsList.as_view(), name='forums_home'),
]
