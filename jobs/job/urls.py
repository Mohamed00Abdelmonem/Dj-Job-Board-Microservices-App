from django.urls import path
from . import views


urlpatterns = [
    path('', views.JobList.as_view()),
    path('<int:pk>/', views.JobDetailUpdateDelete.as_view()),
]