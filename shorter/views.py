from rest_framework.generics import CreateAPIView
from .serializers import ShorterSerializer


class ShorterCreateAPIView(CreateAPIView):
    """
    create api view for create shorter object
    """
    serializer_class = ShorterSerializer
