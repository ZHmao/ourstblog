from django.conf.urls import patterns, include, url
from ourstapp import views
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ourst.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^$', views.homepage),
    (r'^about/$', views.about),
    (r'^contact/$', views.contact),
    (r'^article/(.{1,8})/$', views.blog),
	(r'^undev/$', views.undev),
	(r'^contact/send/$', views.send_to_me),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', 
	{'document_root': settings.STATICFILES_DIRS,}),
)
