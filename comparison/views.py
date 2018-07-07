
from django.apps import apps
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.utils.translation import ugettext as _


def add(request, product_id):

    product = get_object_or_404(
        apps.get_model('products', 'Product'), id=product_id)

    if request.comparison.has_product(product_id):
        message = _('{} already in comparison list')
        messages.error(request, message.format(product.title))

    else:
        request.comparison.add(product)

        message = _('{} added to comparison')
        messages.success(request, message.format(product.name))

    return redirect(request.GET.get('next', 'home'))


def remove(request, product_id):

    product = get_object_or_404(
        apps.get_model('products', 'Product'), id=product_id)

    request.comparison.remove(product_id)

    message = _('{} removed from comparison')
    messages.success(request, message.format(product.name))

    return redirect(request.GET.get('next', 'home'))


def clear(request):

    request.comparison.clear()

    messages.success(request, _('Comparison list was cleaned'))

    return redirect(request.GET.get('next', 'home'))
