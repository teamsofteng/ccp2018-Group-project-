from django.urls import path
from . import views

urlpatterns = [
        #url(r'^$','views.index',name ='index'),
        path('', views.homeactual.as_view(), name = 'Homepage'),
]


