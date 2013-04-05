from django.conf.urls import patterns, include, url
#from core.views import search_it, image_grid
from core import views

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import DetailView
from open_image.models import Article
from django.views.generic import TemplateView
from django.contrib.auth.views import password_reset, password_reset_confirm
import registration.backends.default.urls as regUrls
from registration.views import register
#from member.regbackend import UserRegistrationForm


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^dashboard/', include('member.urls')),
#     url(r'^$', SearchView.as_view(), name='search_it'),
     url(r'^$', 'core.views.search_it', name='search_it'),
     url(r'^den/(?P<slug>.*)/$', 'core.views.image_grid', name='image_grid'),
#     url(r'^userden/(?P<slug>.*)/$', 'core.views.userimage_grid', name='userimage_grid'),
    url(r'^dashboard/mydens/$', views.MyDenListView.as_view(), name='mydens'),
     url(r'^userden/(?P<slug>.*)/$', views.UserDenListView.as_view(), name='userimage_grid'),
     url(r'^api/(?P<pk>.*)/$', views.ImageObjectApiView.as_view(), name='image_object_api'),
     url(r'^apilist/(?P<slug>.*)/$', views.ImageObjectApiListView.as_view(), name='image_list_api'),
     url(r'^detail/(?P<pk>.*)/$', DetailView.as_view(model=Article, context_object_name="image_detail",), name='image_detail'),
     url('^userden/create/$', views.UserDenCreateView.as_view(), name='create_user_den'),

     url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {"next_page": "/"}, name='auth_logout'),
     url(r'^accounts/password/reset/$', password_reset, {'email_template_name': 'email_password_reset.txt', 'subject_template_name': 'email_password_reset_title.txt', 'template_name': 'password_reset.html'}, name='password_reset'),
     url(r'^accounts/password/reset/done/$', TemplateView.as_view(template_name="password_reset_sent.html"), name='password_reset_sent'),
     url(r'^accounts/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {"template_name": "password_reset_confirm.html"}, name='password_reset_confirm'),
     url(r'^accounts/', include('registration.backends.default.urls')),
#    url(r'^accounts/register/$', register, {'backend': 'registration.backends.default.DefaultBackend','form_class': UserRegistrationForm}, name='registration_register'),(r'^accounts/', include(regUrls)),

    #     url(r'^api/latest-image/(?P<search_term>.*)/$', get_latest_image),

     url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$',
         'django.views.static.serve', {'document_root':'./imagesden/media/'}),)