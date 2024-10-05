from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def current_time(context, format_string='%Y-%m-%d %H:%M:%S'):
    return datetime.now().strftime(format_string)