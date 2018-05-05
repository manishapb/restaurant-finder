from django.urls import path
from .views import *
from django.conf.urls import url

app_name = 'resto'

urlpatterns = [
    url(r'^create/', RestoCreateView.as_view(), name='create'),
    url(r'^list/', ListRestoView.as_view(), name = 'list'),
    url(r'^(?P<pk>\d+)/$', DetailRestoView.as_view(), name='resto_detail'),
    url(r'^add-items/(?P<resto_id>\d+)/$', AddDishView.as_view(), name='add_items'),
    url(r'^search/', search, name='search'),
    url(r'^dish/(?P<dish_id>\d+)/$', DishDetailView.as_view(), name='dish_detail'),
]
