"""
URL configuration for locallibrary_pps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.template.defaulttags import url
from django.urls import path, include, re_path
from django.views.static import serve
from photologue import sitemaps
from photologue.sitemaps import GallerySitemap, PhotoSitemap

import booking

sitemaps = {
    'photologue_galleries': GallerySitemap,
    'photologue_photos': PhotoSitemap,
}

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('booking/', include('booking.urls')),
                  path('members/', include('members.urls')),
                  path('members/', include('django.contrib.auth.urls')),
                  path('user', include('members.urls')),
                  path('', include('catalog.urls')),
                  path('', include('booking.urls')),
                  re_path(r'^photologue/', include('photologue.urls', namespace='photologue')),
                  path(
                      "sitemap.xml",
                      sitemap,
                      {"sitemaps": sitemaps},
                      name="django.contrib.sitemaps.views.sitemap",
                  ),

                  re_path(r'^media/(?P<path>.*)$', serve, {'document_root':
                                                               settings.MEDIA_ROOT}),  # serve media files when deployed
                  re_path(r'^static/(?P<path>.*)$', serve, {'document_root':
                                                                settings.STATIC_ROOT}),
                  # serve static files when deployed

              ] + static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)
