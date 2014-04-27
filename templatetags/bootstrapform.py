# -*- coding: utf-8 -*-
from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.filter
def bootstrapform(form):
    return render_to_string('bootstrapform.html', { 'form': form })

@register.filter
def bootstrapform_field_widget(value):
    return value.as_widget(attrs={'class': 'form-control'})

@register.filter
def bootstrapform_field_id(field):
    try:
        widget = field.field.widget
    except AttributeError:
        widget = field.widget
    return widget.attrs.get(id, field.auto_id)
