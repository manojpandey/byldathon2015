from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

from main.views import AddcontactView, AddresourceView, ContactDetailView
from main.models import Contact

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ListView.as_view(
    		model = Contact,
    		queryset = Contact.objects.all(),
    		context_object_name = "contacts",
    		template_name = 'contact/index.html')),
    # url(r'^addcontact/', AddcontactView.as_view()),
    url(r'^add/', AddresourceView.as_view()),
    url(r'^(?P<slug>[-_\w]+)/$', ContactDetailView.as_view(), name='article-detail'),
)
