
from django import template

register = template.Library()


@register.filter(takes_context=True)
def is_compared(object_id, request):
    return request.comparison.has_product(object_id)
