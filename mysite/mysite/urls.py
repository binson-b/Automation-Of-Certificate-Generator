from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from material.frontend import urls as frontend_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('certificates.urls')),
]
