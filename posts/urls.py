from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('hashtags/<int:id>/', views.hashtags, name="hashtags"),
    path('<int:id>/like/', views.like, name="like"),

    path('<int:id>/indexfollow/', views.follow, name="follow"),

    path('<int:id>/create_comment/', views.create_comment, name="create_comment"),
    path('<int:id>/delete_comment/', views.delete_comment, name="delete_comment"),
]

