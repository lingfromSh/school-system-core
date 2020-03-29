from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

EXPIRATION = 30 * 60


class BaseModelViewSet(ModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        cache_key = f"{self.serializer_class.Meta.model.__name__}::{kwargs.get('pk')}"
        if not cache.get(cache_key):
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = serializer.data
            cache.set(cache_key, data, EXPIRATION)
        else:
            data = cache.get(cache_key)
        return Response(data)

    def list(self, request, *args, **kwargs):
        model_name = self.serializer_class.Meta.model.__name__
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            cached_data = cache.get_many(
                (f"{model_name}:{item.pk}" for item in page)
            )
            page = (
                item for item in page if f"{model_name}:{item.pk}" not in cached_data)
            serializer = self.get_serializer(page, many=True)
            data = serializer.data
            data.extend([item for item in cached_data.values()])
            return self.get_paginated_response(data)
            
        cached_data = cache.get_many(
            (f"{model_name}:{item.pk}" for item in queryset)
        )
        queryset = (
            item for item in queryset if f"{model_name}:{item.pk}" not in cached_data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
