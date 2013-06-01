from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def bootstrap_settings_value(name, default=''):
    return getattr(settings, name, default)
