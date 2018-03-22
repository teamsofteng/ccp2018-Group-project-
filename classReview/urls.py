from django.urls import path
from . import views 

urlpatterns = [
	#url(r'^$','views.index',name ='index'),
	path('', views.home.as_view(), name = 'index'),
]
