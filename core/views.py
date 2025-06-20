from operator import attrgetter
from django.contrib import messages
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    TemplateView,
)


class IndexView(TemplateView):
    template_name = "core/index.html"
