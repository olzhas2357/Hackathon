from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ContentViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'contents', ContentViewSet)

urlpatterns = router.urls
