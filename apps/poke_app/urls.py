from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^dashboard', views.dashboard),
    url(r'^givepoke/(?P<user_id>\d+)$', views.givepoke),

  
]
