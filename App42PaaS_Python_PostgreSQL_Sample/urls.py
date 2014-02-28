from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'App42PaaS_Python_PostgreSQL_Sample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	
	# sample
	#   (r'^sample/', include('sample.urls')),
	    url(r'^$', 'sample.views.index'),
	    url(r'^sample/save', 'sample.views.save'),
)
