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
    (r'^article/(.{1,8})/$', views.blog),
	(r'^undev/$', views.undev),
	(r'^login/$', 'django.contrib.auth.views.login'),
	(r'^upload/$', views.upload_article),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', 
	{'document_root': settings.STATICFILES_DIRS,}),
)
