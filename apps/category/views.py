from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.category.models import Category
from apps.category.api.serializers import CategorySerializer

class Categories(APIView):
  def get(self, request, format=None):
    products = Category.objects.all()
    serializer = CategorySerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)