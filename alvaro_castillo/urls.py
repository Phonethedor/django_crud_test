from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('read', (views.read.as_view())),
    path('getId', views.getId, name="getId"),
    path('update', views.update, name="update"),
    path('delete', views.delete, name="delete"),
]