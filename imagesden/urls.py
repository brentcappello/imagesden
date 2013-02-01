from django.conf.urls import patterns, include, url
#from core.views import search_it, image_grid
from core import views

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#     url(r'^$', SearchView.as_view(), name='search_it'),
     url(r'^$', 'core.views.search_it', name='search_it'),
     url(r'^den/(?P<slug>.*)/$', 'core.views.image_grid', name='image_grid'),
     url(r'^api/(?P<pk>.*)/$', views.ImageObjectApiView.as_view(), name='image_object_api'),
    url(r'^apilist/(?P<slug>.*)/$', views.ImageObjectApiListView.as_view(), name='image_list_api'),
#     url(r'^api/latest-image/(?P<search_term>.*)/$', get_latest_image),

     url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$',
         'django.views.static.serve', {'document_root':'./imagesden/media/'}),)