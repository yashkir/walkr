from django.urls import path

from . import views

urlpatterns = [
    path('', views.ForumList.as_view(), name='forums_home'),
    path('<int:pk>/', views.ForumDetail.as_view(), name='forums_detail'),
]
