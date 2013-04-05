from django.conf.urls import patterns, url
from member.views import DashboardView, AccountView


urlpatterns = patterns('',
    url(r'^$', DashboardView.as_view(), name='dashboard-index'),
    url(r'^account/$', AccountView.as_view(), name='account'),
    url(r'^account/edit/$', 'member.views.profileedit', name="edit-profile"),
    url(r'^account/pass/$', 'member.views.passchange', name="change-password"),



    #       url(r'^profile/(?P<slug>[-\w]+)/$', 'member.views.profileedit'),
    #       url(r'^profile/$', ProfileView.as_view(), name="edit-profile"),
)