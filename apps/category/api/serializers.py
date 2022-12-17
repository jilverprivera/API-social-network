from rest_framework import serializers

from apps.category.models import *

class CategorySerializer(serializers.ModelSerializer):
  created_at = serializers.SerializerMethodField()
  class Meta:
    model= Category
    fields = (
      'name', 
      'slug', 
      'created_at'
    )
  
  def get_created_at(self, obj):
    return obj.created_at.strftime('%d-%m-%Y, %H:%M:%S')