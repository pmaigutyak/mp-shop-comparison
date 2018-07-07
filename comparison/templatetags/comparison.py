
from django import template

register = template.Library()


class CheckProductNode(template.Node):

    def __init__(self, parser, token):

        bits = token.split_contents()

        assert len(bits) == 2

        self._product_id = parser.compile_filter(bits[1])

        self._nodelist_if = parser.parse(('else', 'endif', ))

        if parser.next_token().contents == 'else':
            self._nodelist_else = parser.parse(('endif', ))
            parser.delete_first_token()

    def render(self, context):

        product_id = self._product_id.resolve(context)

        if context['request'].comparison.has_product(product_id):
            return self._nodelist_if.render(context)

        if hasattr(self, '_nodelist_else'):
            return self._nodelist_else.render(context)

        return ''


@register.tag
def if_product_in_comparison(parser, token):
    return CheckProductNode(parser, token)
