# MP-Shop | Comparison

### Installation:

1) Install using PIP:
```
pip install django-mp-shop-comparison
```

2) Add `'comparison'` to `INSTALLED_APPS`.

3) Add `'comparison.middleware.ComparisonMiddleware'` to `MIDDLEWARE`.

4) Add `path('comparison/', include('comparison.urls'))` to `urlpatterns`.

### Template examples:

```
{% load comparison %}
```

```
{% if_product_in_comparison object.id %}
    <a href="{% url 'comparison:remove' product_id %}?next={{ request.get_full_path }}">
        Remove
    </a>
{% else %}
    <a href="{% url 'comparison:add' product_id %}?next={{ request.get_full_path }}">
        Add
    </a>
{% endif %}
```

```
{% if_product_in_comparison product_id %}
    Product in comparison
{% endif %}
```

```
There are {{ request.comparison|length }} products in comparison
```

```
{% if not request.comparison.is_empty %}
    <ul>
        {% for category in request.comparison.get_categories %}
            <li>
                <a href="{% url 'products:comparison' category.id %}">
                    {{ category.name }}
                </a>
            </li>
        {% endfor %}
    </ul>
{% endif %}
```

### Product list example:

urls.py
```
path('comparison/<int:category_id>/', views.comparison, name='comparison')
```

views.py
```
def comparison(request, category_id):

    category = get_object_or_404(ProductCategory, id=category_id)

    products = request.comparison.get_products(category_id)

    context = {
        'category': category,
        'products': products,
        'attributes': _format_comparison_attrs(category, products)
    }
    return render(request, 'products/comparison.html', context)


def _format_comparison_attrs(category, products):

    attrs = []

    attributes = category.attributes.visible()

    values = {attr.id: {} for attr in attributes}

    for attr_val in ProductAttrValue.objects.filter(
            attr__in=attributes, product__in=products):

        values[attr_val.attr_id][attr_val.product_id] = attr_val.as_html()

    for attr in attributes:
        attrs.append({
            'name': attr.name,
            'values': [values[attr.id].get(p.id) for p in products]
        })

    return attrs
```

### Public methods:

Products count:
```
len(request.comparison)
```

Add to comparison:
```
request.comparison.add(product)
```

Remove from comparison:
```
request.comparison.remove(product_id)
```

Clear comparison list:
```
request.comparison.clear()
```

Check is comparison list empty:
```
request.comparison.is_empty()
```

Get products from comparison:
```
request.comparison.get_products(category_id)
```

Check is product in comparison:
```
request.comparison.has_product(product_id)
```

Get categories of compare products
```
request.comparison.get_categories()
```

### Requirements:
* django >= 2.0.6
* python >= 3.5.2
