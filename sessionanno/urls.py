from django.conf.urls import patterns, include, url
from django.contrib import admin

from anno.views import hello
from anno.views import current_datetime

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sessionanno.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    (r'^hello/$',hello),
    (r'^time/',current_datetime),
)