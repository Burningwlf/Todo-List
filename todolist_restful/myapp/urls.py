from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^list$", ListAPI.as_view())
]