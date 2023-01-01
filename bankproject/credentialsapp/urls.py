from django.urls import path
from credentialsapp import views

app_name='credentialsapp'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('', views.logout, name='logout'),
]
