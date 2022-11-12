from rest_framework.routers import SimpleRouter
from .views import EventView


router = SimpleRouter()
router.register(r'', EventView, basename='event')

urlpatterns = router.urls
