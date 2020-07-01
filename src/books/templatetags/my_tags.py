from django import template

register = template.Library()

@register.simple_tag
def my_first_tag(pk,price):
    return pk+price