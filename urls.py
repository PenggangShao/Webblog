from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'webblog.views.home'),
    url(r'^login/','webblog.views.login'),
    url(r'^logout$','webblog.views.logout'),
    url(r'^register_index$','webblog.views.register'),
    url(r'^register$','webblog.views.register_index'),
    url(r'^admin/', include(admin.site.urls)),
)
