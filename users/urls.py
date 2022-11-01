from django.urls import path, include
from .views import RegisterView, ProfileView, OnlyRetrieve

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profiles/<int:pk>/', OnlyRetrieve.as_view(), name='profile'),
]
