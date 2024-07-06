from django import template
import markdown
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="truncate")
def truncate_chars(value, num):
    """Replace extra text with ... if a post has too many words"""
    if len(value) > num:
        return value[:num] + "..."
    return value


@register.filter(name="markdown")
@stringfilter
def render_markdown(value):
    md = markdown.Markdown(extensions=["fenced_code", "codehilite"])
    html = md.convert(value)

    # Add TailwindCSS classes to the generated HTML
    html = html.replace("<h1>", '<h1 class="text-3xl font-bold">')
    html = html.replace("<h2>", '<h2 class="text-2xl font-semibold">')
    html = html.replace("<h3>", '<h3 class="text-xl font-semibold">')
    html = html.replace("<h4>", '<h4 class="text-lg font-semibold">')
    html = html.replace("<h5>", '<h5 class="text-base font-semibold">')
    html = html.replace("<h6>", '<h6 class="text-sm font-semibold">')
    html = html.replace("<p>", '<p class="mb-4">')
    html = html.replace("<ul>", '<ul class="list-disc ml-5">')
    html = html.replace("<ol>", '<ol class="list-decimal ml-5">')
    html = html.replace("<li>", '<li class="mb-2 text-red-500">')
    html = html.replace("<code>", '<code class="bg-gray-100 p-1 rounded">')
    html = html.replace(
        "<pre>", '<pre class="bg-gray-100 p-4 rounded mb-4 overflow-auto">'
    )

    return mark_safe(html)
