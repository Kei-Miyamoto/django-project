from django.urls import path, include
from rest_framework import routers
from .users import users_views
from .users.users_views import UserView
from app import views

app_name = 'app'
router = routers.DefaultRouter()
router.register(r'users/', UserView)


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('users', UserView.as_view(), name='users'),
]