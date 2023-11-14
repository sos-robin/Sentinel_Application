# custom_filters.py

from django import template

register = template.Library()

@register.filter
def get_first_character(value):
    if value:
        return value[0]
    return ''
