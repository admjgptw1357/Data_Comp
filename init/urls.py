from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import app.views

# Examples:
# url(r'^$', 'init.views.home', name='home'),
urlpatterns = [
    url(r'^$', app.views.index, name='index'),
    # url(r'^db', app.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'logout.html'}),
    url(r'^competition/', include("app.urls",namespace="app")),

]
# url(r'^blog/', include('blog.urls')),


urlpatterns += staticfiles_urlpatterns()
