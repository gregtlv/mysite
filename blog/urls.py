from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_last, name='post_last') # it is function name in views.py
]
