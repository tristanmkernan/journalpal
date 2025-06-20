from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class JournalEntryQuerySet(models.QuerySet):
    def for_user(self, user):
        return self.filter(creator=user)


class JournalEntry(models.Model):
    objects = JournalEntryQuerySet.as_manager()

    uuid = models.UUIDField(default=uuid4, unique=True, editable=False)

    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    raw_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Journal Entry by {self.creator} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
