from django.urls import path

from . import views

urlpatterns = [
    path('shop/greetings/', views.greetings, name='greetings'),
]