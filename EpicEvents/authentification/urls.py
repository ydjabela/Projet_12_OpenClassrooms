from rest_framework.routers import SimpleRouter
from .views import ClientView


router = SimpleRouter()
router.register(r'', ClientView, basename='client')

urlpatterns = router.urls
