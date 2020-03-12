# MP-Shop | Comparison

### Installation:

1) Install using PIP:
```
pip install django-mp-shop-comparison
```

2) Add `'comparison'` to `INSTALLED_APPS`.

3) Add `'comparison.middleware.ComparisonMiddleware'` to `MIDDLEWARE`.

4) Add `path('comparison/', include('comparison.urls'))` to `urlpatterns`.


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
