from django import urls
from django.urls import path
from . import views

urlpatterns=[
    path('graph-plot', views.graphPlot, name='Graph plot page' ),
    
    path('graph-plot/get-skyplot-data', views.sendGSVData, name="Function to send data of GSV from database"),

    path('gnss-satellite-data', views.recievingGSVData, name="API to recieve satellite data from"),

    path('index-gnss', views.gnss, name="gnss page"),

    path('gnss-constillations', views.gnssConstillations, name="gnss-constillations page"),

    path('gnss-stations-worldwide', views.gnssStationsWorldwide, name="gnss-stations-worldwide page"),

    path('gnss-gallery', views.gnssGallery, name="gnss-gallery page"),

    path('gnss-experts', views.gnssExperts, name="gnss-experts page"),
]