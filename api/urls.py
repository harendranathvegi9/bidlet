from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.BidletList.as_view(), name='bidlet-list'),
]
