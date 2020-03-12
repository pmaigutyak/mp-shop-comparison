
from django.conf import settings

from comparison import defaults


COMPARISON_CATEGORY_MODEL = getattr(
    settings, 'COMPARISON_CATEGORY_MODEL', defaults.COMPARISON_CATEGORY_MODEL)

COMPARISON_PRODUCT_MODEL = getattr(
    settings, 'COMPARISON_PRODUCT_MODEL', defaults.COMPARISON_PRODUCT_MODEL)
