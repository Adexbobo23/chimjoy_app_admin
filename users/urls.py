from django.urls import path
from .views import ( 
    home, user_login, register, 
    profile, error, orders, favorite,
    dashboard, custom_logout, password_reset_request, password_reset
    )

urlpatterns = [
    path('home/', home, name='home'),
    path('register/', register, name='registerr'),
    path('login/', user_login, name='loginn'),
    path('profile/', profile, name='profilee'),
    path('error/', error, name='error'),
    path('orders/', orders, name='orders'),
    path('favorite/', favorite, name='favorite'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', custom_logout, name='logoutt'),
    path('password_reset/', password_reset_request, name='password_reset_request'),
    path('password_reset/<str:uidb64>/<str:token>/', password_reset, name='password_reset'),
]