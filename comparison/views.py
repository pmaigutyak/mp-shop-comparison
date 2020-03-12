
from django.apps import apps
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.translation import ugettext as _
from django.views.decorators.http import require_POST
from django.http.response import JsonResponse
from django.template.loader import render_to_string

from comparison.config import COMPARISON_CATEGORY_MODEL


def index(request, category_id):

    category_model = apps.get_model(COMPARISON_CATEGORY_MODEL)

    category = get_object_or_404(category_model, id=category_id)

    products = request.comparison.get_products(category_id)

    context = {
        'category': category,
        'products': products,
    }

    if apps.is_installed('attributes'):
        from attributes.utils import format_attributes
        context['attributes'] = format_attributes(
            category, [p.id for p in products])

    return render(request, 'comparison/index.html', context)


@require_POST
@csrf_exempt
def toggle(request, product_id):

    if request.comparison.has_product(product_id):
        return remove(request, product_id)

    return add(request, product_id)


@require_POST
@csrf_exempt
def add(request, product_id):
    return _action_view(
        request,
        product_id,
        action=lambda p: request.comparison.add(p),
        message=lambda p: _('{} added to comparison').format(p.name))


@require_POST
@csrf_exempt
def remove(request, product_id):
    return _action_view(
        request,
        product_id,
        action=lambda p: request.comparison.remove(p),
        message=lambda p: _('{} removed from comparison').format(p.name))


def _action_view(request, product_id, action, message):

    product = get_object_or_404(
        apps.get_model('products', 'Product'), id=product_id)

    action(product)

    if not request.is_ajax():
        return redirect(request.POST.get('next', 'home'))

    return JsonResponse({
        'message': message(product),
        'dropdown': render_to_string(
            'comparison/dropdown.html', request=request),
        'is_active': request.comparison.has_product(product_id)
    })
