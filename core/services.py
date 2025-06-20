from django.conf import settings
from openai import OpenAI
from pydantic import BaseModel

from core.enums import Sentiment
from core.models import JournalEntry


class JournalEntryEnrichment(BaseModel):
    sentiment: Sentiment
    summary: str


_client = None


def get_client() -> OpenAI:
    global _client

    if _client is None:
        _client = OpenAI(api_key=settings.OPENAI_API_KEY)

    return _client


SYSTEM_PROMPT = """
You are a helpful journaling assistant for kind, caring and loving human beings, seeking to better themselves through introspection and self development.

For the following journal entry, please provide the following:

- a sentiment that categories the entry's mood and tone
- a short, 1-3 sentence summary of the entry, including key events. This summary should be from the perspective of the person writing the journal. For example, if the person writes about their day, assume the human's perspective and use I statements like "I went to the cafe today".
"""


def enrich_journal_entry(entry: JournalEntry) -> None:
    client = get_client()

    response = client.responses.parse(
        model=settings.OPENAI_MODEL,
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": str(entry.raw_text),
            },
        ],
        text_format=JournalEntryEnrichment,
    )

    enrichment = response.output_parsed

    entry.summary = enrichment.summary
    entry.sentiment = enrichment.sentiment
    entry.save()
