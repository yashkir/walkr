from django.urls import path

from . import views

urlpatterns = [
    path('', views.ForumsList.as_view(), name='forums_home'),
    path('<int:pk>/', views.ForumsDetail.as_view(), name='forums_detail'),
]
