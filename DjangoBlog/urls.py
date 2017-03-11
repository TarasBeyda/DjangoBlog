from django.conf.urls import url
from django.contrib import admin
from blog.views import home, about

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about')
]