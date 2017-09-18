from django.conf.urls import url                                                
                                                                                
from main import views                                                          
                                                                                
urlpatterns = [                                                                 
    url(r'^$', views.main, name='main'),
    url(r'downloads-cairam/$', views.downloads_drop, name='downloads_drop'),
    url(r'^thanks/$', views.thanks, name='thanks'),
]
