from django.conf.urls import patterns, include, url
from core.views import search_it

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#     url(r'^$', SearchView.as_view(), name='search_it'),
     url(r'^$', 'core.views.search_it', name='search_it'),

     url(r'^admin/', include(admin.site.urls)),
)
