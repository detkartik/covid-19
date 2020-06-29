from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    ''' 
    URL redirection to home page as it is single page application hence it redirects the url to index.html
    '''
    url('^$',views.index, name='index'),
]
