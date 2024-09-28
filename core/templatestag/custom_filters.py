from django import template
register = template.Library()

@register.filter
def format_vnd(value):
    return "{:,.0f}₫".format(value).replace(",", ".")