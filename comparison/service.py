
from django.apps import apps


SESSION_KEY = 'COMPARISON'


class Comparison(object):

    Product = apps.get_model('products', 'Product')
    ProductCategory = apps.get_model('products', 'ProductCategory')

    def __init__(self, session):

        self.session = session

        self._product_ids = self.session.get(SESSION_KEY, [])

    @property
    def _products(self):

        if hasattr(self, '_products_cache'):
            return self._products_cache

        self._products_cache = {}

        if self._product_ids:
            for product in self.Product.objects.filter(
                    id__in=self._product_ids):
                self._products_cache[product.pk] = product

        return self._products_cache

    def __len__(self):
        return len(self._product_ids)

    def _update_session(self):
        self.session[SESSION_KEY] = self._product_ids
        self.session.modified = True

    def add(self, product):

        if product.id not in self._products:
            self._product_ids.append(product.id)
            self._products_cache[product.id] = product
            self._update_session()

    def remove(self, product_id):
        if product_id in self._product_ids:
            self._product_ids.remove(product_id)

            if hasattr(self, '_products_cache'):
                del self._products_cache[product_id]

            self._update_session()

    def clear(self):
        if hasattr(self, '_products_cache'):
            self._products_cache = {}
            self._update_session()

    def is_empty(self):
        return len(self._product_ids) == 0

    def get_products(self, category_id):

        products = []

        for product in self._products.values():
            if product.category_id == category_id:
                products.append(product)

        return products

    def has_product(self, product_id):
        return product_id in self._product_ids

    def get_categories(self):
        return self.ProductCategory.objects.filter(
            products__in=self._products.keys()).distinct()
