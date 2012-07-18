from django.conf.urls import patterns, include, url

urlpatterns = patterns('comment.views',
    url(r'^post/$', 'post'),
)
