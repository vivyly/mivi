import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mivi.views.index', name='mivi_index'),
    url(r'^travels', include('adventures.urls')),
    #url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^sfblog/', include('sfblog.urls')),
)

#urlpatterns += patterns(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'/static/'})

