from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Fieldset, Layout, Submit
from django import forms
from django.urls import reverse

from .models import JournalEntry


class JournalEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.layout = Layout(
            Fieldset(
                "Add Journal Entry",
                "raw_text",
            ),
            Submit("submit", "Create"),
        )

        self.helper.form_action = reverse("core:journal_create")

    class Meta:
        model = JournalEntry
        fields = [
            "raw_text",
        ]
