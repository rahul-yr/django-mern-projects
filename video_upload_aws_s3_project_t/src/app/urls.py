"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from video_files.views import home,upload,fetch_url,get_upload_pre_sign_url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('upload',upload,name='upload'),
    path('fetch-url',fetch_url,name='fetch_url'),
    path('sign-s3',get_upload_pre_sign_url,name='get_upload_pre_sign_url'),

]


if not settings.USE_S3:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)