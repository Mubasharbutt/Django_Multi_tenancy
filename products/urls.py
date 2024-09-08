from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,BusinessProductListView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('business/<int:business_id>/products/', BusinessProductListView.as_view(), name='business-products'),

]
