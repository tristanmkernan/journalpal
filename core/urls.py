from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
