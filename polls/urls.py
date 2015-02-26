from django.conf.urls import patterns,url
from polls import views
from django.conf import settings
urlpatterns = patterns('',url(r'^$',views.index,name = 'index'),
    url(r'^(?P<question_id>\d+)/$',views.detail,name = 'detail'),
    url(r'^(?P<question_id>\d+)/vote/$',views.vote,name = 'vote'),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
)