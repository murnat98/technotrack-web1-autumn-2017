from django.conf.urls import url
from ads.views import *

category_regexp = '(?P<category>\S+)'

urlpatterns = [
    url(r'^' + category_regexp + '/$', category_view),
    url(r'^' + category_regexp + '/(?P<post_id>\d+)$', post_detail),
]
