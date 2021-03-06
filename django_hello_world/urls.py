from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', name='auth_login'),
    url(r'^$', 'django_hello_world.hello.views.home', name='home'),
    # url(r'^django_hello_world/', include('django_hello_world.foo.urls')),
    url(r'^contacts/edit/$', 'django_hello_world.hello.views.edit_contacts', name='edit_contacts'),
    url(r'^requests/$', 'django_hello_world.hello.views.requests', name='requests_list'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
