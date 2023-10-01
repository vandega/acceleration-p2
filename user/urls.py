from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserCreateAPIView.as_view(), name='registration'),
    path('all/', views.UserListAPIView.as_view(), name='user_list'),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('logout/', views.UserLogoutAPIView.as_view(), name='logout'),
    path('profile/', views.UserEditAPIview.as_view(), name='profile')
]