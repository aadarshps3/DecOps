from django.urls import path

from DecApp import views

urlpatterns = [
    path('', views.Index, name='Index')
]
