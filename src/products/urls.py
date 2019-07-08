
from django.conf.urls import url

from django.urls import path, include, re_path
app_name="products"


from products.views import (
	ProductListView,
	# product_list_view, 
	# ProductDetailView,
	ProductDetailSlugView,
	# product_detail_view,
	# ProductFeaturedListView,
	# ProductFeaturedDetailView
    )

urlpatterns = [
    url(r"^$",ProductListView.as_view(),name='list'),
    url(r"^(?P<slug>[\w-]+)/$",ProductDetailSlugView.as_view(),name='detail'),

]



