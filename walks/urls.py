from django.urls import path
#add something here
from . import views

urlpatterns = [
    path('', views.WalksList.as_view(), name='walks_home'),
    path('create_walk/', views.WalkCreate.as_view(), name="create_walk"),
    path('<int:walk_id>/add_stop/', views.StopCreate.as_view(), name="create_stop"),
    path('<int:walk_id>/stop/<int:stop_id>/add_photo/', views.PictureCreate.as_view(), name="create_picture"),
    path('all_walks/', views.WalksList.as_view(), name='all_walks'),
    path('view_walk/<int:pk>/', views.WalkDetail.as_view(), name = 'walk_detail'),
    path('view_walk/<int:pk>/edit', views.WalkEdit.as_view(), name = 'walk_edit'),
    path('view_walk/<int:pk>/delete', views.WalkDelete.as_view(), name = 'walk_delete'),
    path('<int:walk_id>/stop/<int:stop_id>/', views.StopDetail.as_view(), name='stop_detail'),
    path('<int:walk_id>/stop/<int:stop_id>/edit', views.StopEdit.as_view(), name='edit_stop'),
    path('<int:walk_id>/stop/<int:stop_id>/delete', views.StopDelete.as_view(), name='delete_stop'),
]