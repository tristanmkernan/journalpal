from django import template

register = template.Library()


@register.filter
def sentiment_badge_class(sentiment):
    classes = {
        "positive": "badge bg-success",
        "negative": "badge bg-danger",
        "neutral": "badge bg-secondary",
    }
    return classes.get(sentiment, "badge bg-light text-dark")
