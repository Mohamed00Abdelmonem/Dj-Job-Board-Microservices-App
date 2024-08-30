from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListAPI.as_view()),
    path('<int:pk>/', views.PostDetailAPI.as_view()),
    path('add-like', views.PostLikesAPI.as_view()),
    path('add-comment', views.CreateCommetAPI.as_view()),
    
    
    ]