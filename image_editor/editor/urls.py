from django.urls import path
from . import views

app_name = 'editor'

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/', views.edit_image, name='edit_image'),
]
