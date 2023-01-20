from django.urls import include, path
from rest_framework import routers

from user import views as user_views
from credits_score import views as credits_views

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='user')
router.register(r'debts', user_views.DebtViewSet, basename='debt')
router.register(r'credits', credits_views.CreditScoreViewSet, basename='credit')
router.register(r'assets', credits_views.AssetViewSet, basename='asset')
router.register(r'credit_requests', credits_views.CreditRequestViewSet, basename='credit_request')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
