from django.urls import path
from . import views


app_name = 'property'

urlpatterns = [
    path('', views.property_list , name='property_list'),
    path('<slug:category_slug>' , views.property_list , name='property_list_category') ,
    path('detail/<slug:property_slug>', views.property_detail , name='property_detail'),
]
