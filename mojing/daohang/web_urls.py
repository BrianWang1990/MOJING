from django.conf.urls import url
import daohang.views.web as web

urlpatterns = [
    url(r'^index.html', web.index_view),
]
