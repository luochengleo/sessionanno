from django.conf.urls import patterns, include, url
from django.contrib import admin

from anno.views import hello
from anno.views import current_datetime
from anno.views import train
from anno.views import search
from anno.views import validate
from anno.views import login


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sessionanno.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    (r'^hello/$',hello),
    (r'^time/',current_datetime),
    (r'^search/(\d{1,2})/(.*?)/(\d{1,2})/$',search),
    (r'^train/(\d{1,2})/$',train),
    (r'^validate/(\d{1,2})/$',validate),
    (r'^login/$',login),


)