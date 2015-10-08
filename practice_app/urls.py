from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView


from practice_app.views import *

urlpatterns = patterns('',
    
#     url(r'^finance/$', TemplateView.as_view(template_name="finance.html"), name='finance'),
     url(r'', main_page, name='main_page'),
    
 )