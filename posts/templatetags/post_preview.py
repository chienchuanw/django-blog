from django import template

register = template.Library()


@register.filter(name="truncate")
def truncate_chars(value, num):
    """Replace extra text with ... if a post has too many words"""
    if len(value) > num:
        return value[:num] + "..."
    return value
