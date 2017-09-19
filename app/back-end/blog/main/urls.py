from django.conf.urls import url                                                
                                                                                
from main import views                                                          
                                                                                
urlpatterns = [                                                                 
    url(r'^$', views.main, name='main'),
    url(r'downloads-cairam/$', views.downloads_drop, name='downloads_drop'),
    url(r'whatsapp-para-empresas/$', views.whatsapp4business, name='whatsapp4business'),
    url(r'^thanks/$', views.thanks, name='thanks'),
]
