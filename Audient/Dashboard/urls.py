from django.urls import path
from Dashboard import views

urlpatterns = [
    path('posts', views.posts),
]