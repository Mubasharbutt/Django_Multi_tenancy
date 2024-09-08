from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignupView, LoginView, UserDetailView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-detail/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),
]
