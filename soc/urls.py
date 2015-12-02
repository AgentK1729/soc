from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'soc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'soc.alerts.views.home'),
    url(r'^signup/', 'soc.alerts.views.signup'),
    url(r'^profile/', 'soc.alerts.views.profile'),
    url(r'^register/', 'soc.alerts.views.register'),
    url(r'^view-afflictions/', 'soc.alerts.views.afflictions'),
    url(r'^view-diseases/', 'soc.alerts.views.diseases'),
    url(r'^logout/', 'soc.alerts.views.logout'),
)
