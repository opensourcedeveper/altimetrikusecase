from django.urls import path
from .views import FeatureToggleListCreateView, FeatureToggleDetailView

app_name = 'feature_toggle'

urlpatterns = [
    path('toggles/', FeatureToggleListCreateView.as_view(), name='toggle-list'),
    path('toggles/<int:pk>/', FeatureToggleDetailView.as_view(), name='toggle-detail'),
]
