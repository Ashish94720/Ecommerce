
from django.conf.urls import url

from django.urls import path, include, re_path
app_name="search"


from .views import (
	SearchProductView,
    )

urlpatterns = [
    url(r"^$",SearchProductView.as_view(),name='query'),	

]



