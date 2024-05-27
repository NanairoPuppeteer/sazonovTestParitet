from rest_framework import viewsets
from rest_framework.response import Response
from pics.picsapi.models import Picture
from pics.picsapi.serializers import PictureSerializer

# Create your views here.
class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
