from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$',views.login),
	url(r'^search/$',views.search),
	url(r'^details/$',views.details),
]