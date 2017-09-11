from django.conf.urls import url

from . import views

app_name = 'contacts'
urlpatterns = [
        url(r'', views.contactsList, name='contactsList'),
        url(r'^(?P<contact_id>[0-9]+)/$', views.contactsProfile, name = 'contactsProfile'),
]
