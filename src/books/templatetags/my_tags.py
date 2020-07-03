from django import template

register = template.Library()


@register.simple_tag
def my_first_tag(pk,price):
    return pk+price

def rev_name(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value[::-1]

register.filter('rev_name', rev_name)