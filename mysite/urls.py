"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from home import views as home_views
from nasa import views as nasa_views
from trips import views as trips_views

router = routers.DefaultRouter()
router.register(r'nasa', nasa_views.ReportViewSet)
router.register(r'trips', trips_views.PostViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', home_views.index),
    path('trips/', trips_views.index),
    path('trips/details/<int:pk>', trips_views.details, name='details'),
    path('api/trips/create_betch', trips_views.create_betch),
    path('api/nasa/create_betch', nasa_views.create_betch),
    path('api/nasa/get_wind/<lon>/<lat>', nasa_views.get_wind),
    path('api/nasa/get_rain/<lon>/<lat>', nasa_views.get_rain),
    path('api/nasa/get_temp/<lon>/<lat>', nasa_views.get_temp),
    path('api/nasa/get_wind_mean/<lon>/<lat>', nasa_views.get_wind_mean),
    path('api/nasa/get_rain_mean/<lon>/<lat>', nasa_views.get_rain_mean),
    path('api/nasa/get_temp_mean/<lon>/<lat>', nasa_views.get_temp_mean),
]
