from django.conf.urls import url, include
from django.contrib import admin
from blog.views import home, about, show_article

urlpatterns = [
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', show_article, name='article')
]