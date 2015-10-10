from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView


from practice_app import views

urlpatterns = patterns('',
    
#     url(r'^finance/$', TemplateView.as_view(template_name="finance.html"), name='finance'),
     url(r'', views.main_page, name='main_page'),
     url(r'^get_ticker/$',views.get_ticker, name="get_ticker"),
    
 )