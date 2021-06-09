from django.http import JsonResponse
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import generics, response

from .serializers import StatDetailsSerializer, StatQuerySerializer
from statistical_counters.models import Statistics
from .service import StatFilter


class SticticCreateView(generics.CreateAPIView):
    serializer_class = StatDetailsSerializer


class SticticShowView(generics.ListAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatQuerySerializer

    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = StatFilter
    ordering_fields = ['timestamp', 'views', 'clicks', 'cost_of_click', 'cpc', 'cpm']


@api_view(['DELETE'])
@permission_classes([AllowAny])
def reset(request):
    Statistics.objects.all().delete()
    return response.Response(
                status=204,
                data={'status':'true',
                      'message': 'all saved statistics removed'})