from django.conf.urls import url
from scheduleGen.views import Index
from . import views
from django.urls import path
urlpatterns = [
	path('', Index.as_view(), name='home'),
]
