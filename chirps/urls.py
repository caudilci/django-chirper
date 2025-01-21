from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:chirp_id>/edit/", views.edit, name="edit"),
]
