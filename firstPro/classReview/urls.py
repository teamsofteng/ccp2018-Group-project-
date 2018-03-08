from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'index$', views.index),
	#url(r'index/$', classReview.views.index, name = "index"),
]
