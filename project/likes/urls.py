from django.conf.urls import url

from likes.views import LikeView

urlpatterns = [
    url(r'^(?P<pk>\d+)$', LikeView.as_view(), name='like'),
]
