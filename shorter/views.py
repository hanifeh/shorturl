from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import ShorterSerializer
from .models import Shorter
from django.shortcuts import get_object_or_404
from django.utils import timezone


class ShorterCreateAPIView(CreateAPIView):
    """
    create api view for create shorter object
    """
    serializer_class = ShorterSerializer


class ShorterListAPIView(ListAPIView):
    """
    list api view for redirect to original link
    """

    def get(self, request, *args, **kwargs):
        short_url = kwargs.get('shorter')
        try:
            obj = get_object_or_404(Shorter, short_url=short_url)
            if obj.created_time + timezone.timedelta(minutes=obj.validate_time) < timezone.now():
                return JsonResponse({'error': "url expired."}, status=400)
            if obj.status == 'privet':
                if request.data.get('otp') != obj.one_time_password:
                    return JsonResponse({'error': "otp is not correct."}, status=400)
            obj.counter += 1
            obj.save()
            return HttpResponseRedirect(redirect_to=obj.original_url)
        except:
            return JsonResponse({'error': "url not found."}, status=404)
