
from django.urls import path

from comparison import views


app_name = 'comparison'


urlpatterns = [

    path('<int:category_id>/', views.index, name='index'),

    path('add/<int:product_id>/', views.add, name='add'),

    path('remove/<int:product_id>/', views.remove, name='remove'),

    path('toggle/<int:product_id>/', views.toggle, name='toggle')

]
