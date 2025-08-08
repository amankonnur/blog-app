from django.urls import path
from blogapp import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('',views.home, name='home'),
    path('profile/',views.profile,name='profile'),
    path('explore/', views.explore, name='explore'),
]