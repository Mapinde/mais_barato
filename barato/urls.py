from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.produto_lista),
    url(r'^produto/(?P<pro_nome>[\w|\W]+)/(?P<pk>[0-9]+)/$', views.produto_detalhe),
   # url(r'^Produto/(?P<pk>[0-9]+)/$', views.post_detail, name='produto_detalhe'),
    url(r'^sobre/$', views.sobre_nos, name='sobre_nos'),
    url(r'^contact/$', views.contact_us, name='contact_us'),
]
