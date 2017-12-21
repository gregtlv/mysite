from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.vera_main, name='vera_main'), # it is function name in views.py
]
