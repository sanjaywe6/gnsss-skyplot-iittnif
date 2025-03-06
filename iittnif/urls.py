"""
URL configuration for iittnif project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

admin.site.site_header = "IIT Tirupati Navavishkar I-Hub Foundation"
admin.site.site_title = "IITTNiF"

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.index, name='Landing Page'),

    path('irnss/', views.irnss, name="irnss page"),

    path('about-irnss/', views.aboutirnss, name="about-irnss page"),

    path('timeline-irnss/', views.timelineirnss, name="timeline-irnss page"),

    path('ongoing-research-irnss', views.ongoingResearchirnss, name="ongoing-research-irnss page"),

    path('stations-institute-working', views.stationsInstituteWorking, name="stations-institute-working page"),

    path('irnss-gallery', views.irnssGallery, name="irnss-gallery page"),

    path('irnss/research-article/<int:id>/', views.researchArticles, name="researchArticles page"),

    path('data', views.data, name="data page"),

    path('contact-us', views.contactUs, name="contact-us page"),

    path('team', views.team, name="team page"),

    path('gnss/', include('gnss.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
