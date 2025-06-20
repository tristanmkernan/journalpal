from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "core"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
]
