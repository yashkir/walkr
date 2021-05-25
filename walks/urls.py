from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='walks_home'),
    path('createWalk/', views.CreateWalkFormView.as_view(), name="create_walk"),
]
