from django.conf.urls import url

from question.views import CategoriesList, CategoryDetail, QuestionDetail, CreateQuestionView, QuestionList, \
    UpdateQuestionView, UpdateAnswerView, MyQuestionsList, MyAnswersList, DeleteQuestionView

urlpatterns = [
    url(r'^categories/$', CategoriesList.as_view(), name='categories_list'),
    url(r'^categories/(?P<pk>\d+)$', CategoryDetail.as_view(), name='category_detail'),
    url(r'^$', QuestionList.as_view(), name='questions_list'),
    url(r'^(?P<pk>\d+)$', QuestionDetail.as_view(), name='question_detail'),
    url(r'^create_question/$', CreateQuestionView.as_view(), name='create_question'),
    url(r'^update_question/(?P<pk>\d+)$', UpdateQuestionView.as_view(), name='update_question'),
    url(r'^delete_question/(?P<pk>\d+)$', DeleteQuestionView.as_view(), name='delete_question'),
    url(r'^update_answer/(?P<pk>\d+)$', UpdateAnswerView.as_view(), name='update_answer'),
    url(r'^my_questions/$', MyQuestionsList.as_view(), name='my_questions'),
    url(r'^my_answers/$', MyAnswersList.as_view(), name='my_answers'),
]
