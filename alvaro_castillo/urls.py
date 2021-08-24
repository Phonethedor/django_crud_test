from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('read', (views.read.as_view())),
    path('update', views.delete, name="update"),
    path('getId', views.getId, name="getId"),
]