from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, DestinationViewSet, IncomingViewSet

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'destinations', DestinationViewSet)
router.register(r'incomings', IncomingViewSet, basename='incoming')

urlpatterns = [
    path('', include(router.urls)),
]