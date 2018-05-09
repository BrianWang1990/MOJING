from django.conf.urls import url
from django.urls import path
import daohang.views.web as web

urlpatterns = [
    url(r'^index.html', web.index_view),
]
