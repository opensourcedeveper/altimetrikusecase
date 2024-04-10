from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import FeatureToggle
from .serializers import FeatureToggleSerializer

class FeatureToggleListCreateView(generics.ListCreateAPIView):
    queryset = FeatureToggle.objects.all()
    serializer_class = FeatureToggleSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        created_by = self.request.query_params.get('created_by', None)
        if created_by:
            queryset = queryset.filter(created_by=created_by)
        return queryset

class FeatureToggleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeatureToggle.objects.all()
    serializer_class = FeatureToggleSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        is_enabled = request.data.get('is_enabled', None)
        if is_enabled is not None:
            instance.is_enabled = is_enabled
            instance.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
