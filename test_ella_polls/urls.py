from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^polls', include('ella_polls.urls')),
    (r'^', include('ella.core.urls')),
)
