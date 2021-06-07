from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create', views.create, name='create'),
    path('success_saved', views.success_saved, name='success_saved'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]