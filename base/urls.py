from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_page, name="register"),
    path('', views.home, name="home"),
    path('room/<str:id>/', views.room, name="room"),
    path('profile/<str:id>/', views.userProfile, name="user-profile"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:id>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:id>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:id>/', views.deleteMessage, name="delete-message"),
    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicsPage, name="topics")
]
