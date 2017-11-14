from django.conf.urls import url

from question.views import CategoriesList, CategoryDetail, QuestionDetail

urlpatterns = [
    url(r'^categories/$', CategoriesList.as_view(), name='categories_list'),
    url(r'^categories/(?P<pk>\d+)$', CategoryDetail.as_view(), name='category_detail'),
    url(r'^/(?P<pk>\d+)$', QuestionDetail.as_view(), name='question_detail'),
]