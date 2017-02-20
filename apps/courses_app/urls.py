from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^courses$', views.create),
	url(r'^courses/destroy/(?P<course_id>\d+)$', views.delete)
]