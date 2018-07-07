
from django.urls import path

from comparison import views


app_name = 'comparison'


urlpatterns = [

    path('add/<int:product_id>/', views.add, name='add'),

    path('remove/<int:product_id>/', views.remove, name='remove'),

    path('clear/', views.clear, name='clear'),

]
