from django.conf.urls import patterns, include, url
from django.contrib import admin

from labsmith.views import mylogout,redirect2labsmith,register,mylogin,reset,resetresult
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'labsmith.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', redirect2labsmith, name = redirect2labsmith),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^labsmith/', include('device_management.urls')),
    url(r'^login/$', mylogin, name = mylogin),
    url(r'^logout/$', mylogout, name = mylogout),
    url(r'^register/$', register, name = register),

    #url(r'^/labsmith/password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
   # url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),    
   # url(r'^reset/(?P[0-9A-Za-z]+)-(?P.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    #url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^reset/$', reset, name="reset"),
    url(r'^resetresult/$', resetresult, name="resetsult"),
    #url(r'^changePWD/$', mychangePWD, name = mychangePWD),
)
