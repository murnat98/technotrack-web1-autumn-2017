from django.conf.urls import url

from core.views import *

urlpatterns = [
    url(r'^$', show_users, name='show_users'),
    url(r'^(?P<pk>\d+)/$', UserDetail.as_view(), name='user'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
