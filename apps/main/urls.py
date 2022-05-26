from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ProductAPIView, ProductSetView

router = SimpleRouter()
router.register('product', ProductSetView)

urlpatterns = [
    path('lists/', ProductAPIView.as_view()),
    path("create/", include(router.urls)),
]

