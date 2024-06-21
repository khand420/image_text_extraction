from rest_framework import serializers
from .models import ImageText

class ImageTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageText
        fields = '__all__'