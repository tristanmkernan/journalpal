from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    TemplateView,
)


class IndexView(TemplateView):
    template_name = "core/index.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"

    def get_queryset(self):
        pass
