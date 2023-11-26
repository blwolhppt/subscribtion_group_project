from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api import views

router = SimpleRouter()

# router.register('category', views.CategoryViewSet)
# router.register('subscription', views.SubscriptionViewSet)
router.register('users', views.CustomUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken'))
]
