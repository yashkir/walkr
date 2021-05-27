from django.urls import path

from . import views

urlpatterns = [
    path('', views.ForumList.as_view(), name='forums_home'),
    path('<int:pk>/', views.ForumDetail.as_view(), name='forums_detail'),
    path('<int:forum_id>/threads/', views.ThreadCreate.as_view(), name='threads_create'),
    path('threads/<int:pk>/', views.ThreadDetail.as_view(), name='threads_detail'),
    path('threads/<int:pk>/delete', views.ThreadDelete.as_view(), name='threads_delete'),
    path('threads/<int:thread_id>/posts', views.PostCreate.as_view(), name='posts_create'),
    path('threads/<int:thread_id>/posts/<int:post_id>/reply', views.PostReply.as_view(), name='posts_reply'),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name='posts_delete'),
    path('posts/<int:pk>/edit', views.PostEdit.as_view(), name='posts_edit'),
]
