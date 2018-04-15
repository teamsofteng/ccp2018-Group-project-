from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
urlpatterns = [
    	url(r'^$',views.home),
	url(r'^login/$', login,{'template_name': 'account/index.html'}),
	url(r'^logout/$', logout,{'template_name': 'account/index1.html'}),
	url(r'^register/$', views.register, name='register')
]
