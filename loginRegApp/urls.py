from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.Reggae),
    path("success", views.weMadeIt),
    path('approved', views.ImIn),
    path('logout', views.logout)
]