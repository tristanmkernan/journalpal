from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    TemplateView,
)

from .forms import JournalEntryForm
from .models import JournalEntry


class IndexView(TemplateView):
    template_name = "core/index.html"


class DashboardView(LoginRequiredMixin, ListView):
    template_name = "core/dashboard.html"

    def get_queryset(self):
        return JournalEntry.objects.for_user(self.request.user).order_by("-created_at")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context["form"] = JournalEntryForm()

        return context


class JournalEntryCreateView(CreateView):
    model = JournalEntry
    form_class = JournalEntryForm
    success_url = reverse_lazy("core:dashboard")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
