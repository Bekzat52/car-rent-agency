from django.urls import path, include
from .views import RegisterAPIView, LoginView, LogoutView, ChangePasswordView, activate
from password_reset import views, urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<str:activation_code>/', activate),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('password_reset.urls', namespace='password_reset')),
]