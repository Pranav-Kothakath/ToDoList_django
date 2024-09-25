from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('signup/', views.SignUp, name='signup'),
    path('', views.Home, name='home'),
]
    