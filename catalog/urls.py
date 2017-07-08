from django.conf.urls import url

from catalog import views


urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^product/$', views.ProductListView.as_view(), name='product'),
	url(r'^product/(?P<pk>[0-9a-f-]+)/$', views.ProductDetailView.as_view(), name='product-detail'),
	url(r'^ailment/$', views.AilmentListView.as_view(), name="ailment"),
	url(r'^search/$', views.search, name="search"),
	url(r'^search_results/$', views.search_results, name="search_results"),
]