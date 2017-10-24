from django.conf.urls import url
from core.views import *

category_regexp = '(?P<category>\S+)'

urlpatterns = [
    url(r'^$', show_users),
    url(r'^(?P<user_id>\d+)/$', show_user),
]
