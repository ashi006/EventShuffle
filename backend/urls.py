from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateEvent, name="Create Event"),
    path('list', views.GetAllEvents, name="Get All Events"),
    path(r"<id>", views.GetSingleEvent, name="Get an Event"),
]