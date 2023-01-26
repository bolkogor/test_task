from .views import CarViewSet, TruckViewSet, BoatViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'trucks', TruckViewSet, basename='truck')
router.register(r'boats', BoatViewSet, basename='boat')
urlpatterns = router.urls