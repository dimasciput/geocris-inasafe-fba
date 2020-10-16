from django.urls import path, include
from rest_framework import routers

from fba.api_views.hazard_event import HazardEventAPI
from fba.api_views.recent_hazard import RecentHazardList


router = routers.DefaultRouter()
router.register('hazard-event', HazardEventAPI)

urlpatterns = [
    path('hazard-event/recent/', RecentHazardList.as_view(),
         name='recent-hazard-list-api'),
    path('', include(router.urls))
]
