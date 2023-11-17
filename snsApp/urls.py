from django.urls import path
from . import views

app_name = 'snsApp'
urlpatterns = [
    path('', views.index, name='index'),
]