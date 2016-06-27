from django.conf.urls import include, url

import app.views

# Examples:
# url(r'^$', 'init.views.home', name='home'),
urlpatterns = [
    url(r'^list', app.views.competition_list,name='competition_list'),
    url(r'^detail/(?P<id>\d+)$', app.views.competition_detail, name='competition_detail'),
    url(r'^submission/(?P<id>\d+)$', app.views.submission, name='submission'),

]
