from django.conf.urls import url
from scheduleGen.views import Index
from . import views

urlpatterns = [
	url('', Index.as_view(), name='home'),
]
