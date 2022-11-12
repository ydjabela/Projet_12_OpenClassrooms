from rest_framework.routers import SimpleRouter
from .views import ContratView


router = SimpleRouter()
router.register(r'', ContratView, basename='contrat')

urlpatterns = router.urls
