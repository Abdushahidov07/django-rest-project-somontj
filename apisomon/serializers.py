from rest_framework import serializers

from .models import *


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CastumorUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CastumorUser
        fields = "__all__"
