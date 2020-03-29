from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

EXPIRATION = 30 * 60


class BaseModelViewSet(ModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        cache_key = f"{self.serializer_class.Meta.model}::{kwargs.get('pk')}"
        if not cache.get(cache_key):
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = serializer.data
            cache.set(cache_key, data, EXPIRATION)
        else:
            data = cache.get(cache_key)
        return Response(data)
