from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_app.views.home', name='home'),
    # url(r'^Django_app/', include('Django_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     #url(r'^recipe/', include('Django_app.recipe.urls')),
     url(r'^', include('recipe.urls', namespace="recipe")),
     #(r'^myapp/', include('myproject.myapp.urls')),
)
