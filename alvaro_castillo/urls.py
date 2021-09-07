from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('read', (views.read.as_view())),
    path('update', views.update, name="update"),
    path('getId', views.getId, name="getId"),
    path('delete', views.delete, name="delete"),
]