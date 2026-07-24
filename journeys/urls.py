from rest_framework.routers import DefaultRouter

from .views import JourneyViewSet

router = DefaultRouter()
router.register('journeys', JourneyViewSet, basename='journeys')

urlpatterns = router.urls
