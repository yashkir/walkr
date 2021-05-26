from django.urls import path
#add something here
from . import views

urlpatterns = [
    path('', views.WalksList.as_view(), name='walks_home'),
    path('create_walk/', views.WalkCreate.as_view(), name="create_walk"),
    path('<int:walk_id>/add_stop/', views.StopCreate.as_view(), name="create_stop"),
    path('all_walks/', views.WalksList.as_view(), name='all_walks'),
    path('view_walk/<int:pk>/', views.WalkDetail.as_view(), name = 'walk_detail'),
]
