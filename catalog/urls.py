from django.conf.urls import url

from catalog import views
from catalog.models import Product, Order, Ailment

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^product/$', views.ProductListView.as_view(queryset=Product.objects.order_by('isBlend','name')), name='product'),
	url(r'^product/(?P<pk>[0-9a-f-]+)/$', views.ProductDetailView.as_view(), name='product-detail'),
	url(r'^ailment/$', views.AilmentListView.as_view(queryset=Ailment.objects.order_by('name')), name="ailment"),
	url(r'^product_added/$', views.product_added, name='product_added'),
	url(r'^search/$', views.search, name="search"),
	url(r'^search_results/$', views.search_results, name="search_results"),
	url(r'^cart/$', views.cart, name='cart'),
	url(r'^checkout/$', views.checkout, name='checkout'),
	url(r'^clear_cart/$', views.clear_cart, name='clear_cart'),
	url(r'^user_details/$', views.UserDetailsView, name='user_details'),
]