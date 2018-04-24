from django.urls import path
from .views import RestoCreateView, ListRestoView, DetailRestoView
from django.conf.urls import url

app_name = 'resto'

urlpatterns = [
    url(r'^create/', RestoCreateView.as_view(), name='create'),
    url(r'^list/', ListRestoView.as_view(),name = 'list'),
    url(r'^(?P<pk>\d+)/$',DetailRestoView.as_view(),name='resto_detail'),
]
