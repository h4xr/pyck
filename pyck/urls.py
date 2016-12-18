""" pyck URL Configuration """
from django.conf.urls import url, include
from django.contrib import admin
from services.api import ServiceDataResource
from services.views import HomeView

service_data = ServiceDataResource()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(service_data.urls)),
    url(r'^home/', HomeView.as_view()),
]
