from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Business
from .serializers import BusinessSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]
