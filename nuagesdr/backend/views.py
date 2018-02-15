from backend.models import RiskTypesModel, FieldTypesModel, EnumFieldTypesModel
from backend.serializers import RiskTypesSerializer, FieldTypesSerializer, EnumFieldTypesSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics


class RiskTypes_List(generics.ListCreateAPIView):
    queryset = RiskTypesModel.objects.all()
    serializer_class = RiskTypesSerializer


class RiskTypes_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RiskTypesModel.objects.all()
    serializer_class = RiskTypesSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'snippets': reverse('snippet-list', request=request, format=format)
    })  