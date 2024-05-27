from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from pics.picsapi.models import Picture

class PictureSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=True)

    class Meta:
        model = Picture
        fields = ['id', 'description', 'image']
