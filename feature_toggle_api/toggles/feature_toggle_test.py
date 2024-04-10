# toggles/tests.py
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import FeatureToggle
from .serializers import FeatureToggleSerializer

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create(username='testuser', email='test@example.com', password='password')

@pytest.fixture
def feature_toggle(user):
    return FeatureToggle.objects.create(name='Test Toggle', description='Test Description',
                                        environment='Test Environment', created_by=user)

@pytest.mark.django_db
def test_feature_toggle_creation(feature_toggle):
    assert FeatureToggle.objects.count() == 1
    assert FeatureToggle.objects.get(name='Test Toggle').description == 'Test Description'

@pytest.mark.django_db
def test_feature_toggle_retrieval(api_client, feature_toggle):
    response = api_client.get('/api/v1/toggles/')
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Test Toggle'

@pytest.mark.django_db
def test_feature_toggle_update(api_client, feature_toggle):
    data = {'is_enabled': True}
    response = api_client.patch(f'/api/v1/toggles/{feature_toggle.pk}/', data=data)
    assert response.status_code == 200
    assert FeatureToggle.objects.get(pk=feature_toggle.pk).is_enabled is True

@pytest.mark.django_db
def test_feature_toggle_deletion(api_client, feature_toggle):
    response = api_client.delete(f'/api/v1/toggles/{feature_toggle.pk}/')
    assert response.status_code == 204
    assert FeatureToggle.objects.count() == 0

@pytest.mark.django_db
def test_feature_toggle_serializer():
    user = User.objects.create(username='testuser', email='test@example.com', password='password')
    toggle_data = {'name': 'Test Toggle', 'description': 'Test Description', 'environment': 'Test Environment',
                   'created_by': user.pk, 'is_enabled': False}
    serializer = FeatureToggleSerializer(data=toggle_data)
    assert serializer.is_valid()
    toggle = serializer.save()
    assert toggle.name == 'Test Toggle'
    assert toggle.description == 'Test Description'
