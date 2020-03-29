import json
from collections import OrderedDict

from django.core.cache import cache
from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject
from rest_framework.serializers import (HyperlinkedModelSerializer,
                                        ModelSerializer)

from utils.tools import unique_id


class BaseModelSerializer(ModelSerializer):

    def get_translation(self, choices, value):
        for choice in choices.items():
            if value == choice[0]:
                return choice[1]

    def to_internal_value(self, data):
        if isinstance(data, dict) and not data.get("id", None):
            data['id'] = unique_id()
        return super().to_internal_value(data)

    def to_representation(self, instance, save_flag=False):
        """
        Object instance -> Dict of primitive datatypes.
        """
        cache_key = f"{self.Meta.model.__name__}:{instance.pk}"
        if cache.get(cache_key) and not save_flag:
            return cache.get(cache_key)
        ret = OrderedDict()
        fields = self._readable_fields
        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue
            # We skip `to_representation` for `None` values so that fields do
            # not have to explicitly deal with that case.
            #
            # For related fields with `use_pk_only_optimization` we need to
            # resolve the pk value.
            check_for_none = attribute.pk if isinstance(
                attribute, PKOnlyObject) else attribute
            if check_for_none is None:
                ret[field.field_name] = None
            elif hasattr(field, 'choices'):
                ret[field.field_name] = self.get_translation(
                    field.choices, attribute)
            else:
                ret[field.field_name] = field.to_representation(attribute)

        cache.set(cache_key, ret)

        return ret

    def create(self, validated_data):
        return super().create(validated_data)

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        self.to_representation(instance, save_flag=True)
        return instance


class BaseHyperLinkedModelSerializer(HyperlinkedModelSerializer):
    def get_translation(self, choices, value):
        for choice in choices.items():
            if value == choice[0]:
                return choice[1]

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        cache_key = f"{self.Meta.model.name}:{instance.pk}"
        if cache.get(cache_key):
            return cache[cache_key]
        ret = OrderedDict()
        fields = self._readable_fields
        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue
            # We skip `to_representation` for `None` values so that fields do
            # not have to explicitly deal with that case.
            #
            # For related fields with `use_pk_only_optimization` we need to
            # resolve the pk value.
            check_for_none = attribute.pk if isinstance(
                attribute, PKOnlyObject) else attribute
            if check_for_none is None:
                ret[field.field_name] = None
            elif hasattr(field, 'choices'):
                ret[field.field_name] = self.get_translation(
                    field.choices, attribute)
            else:
                ret[field.field_name] = field.to_representation(attribute)

        cache.set(cache_key, {key: value for key, value in ret.items()})
        return ret

    def to_internal_value(self, data):
        if not data.get("id", None):
            data['id'] = unique_id()
        return super().to_internal_value(data)

    def create(self, validated_data):
        return super().create(validated_data)

    def to_internal_value(self, data):
        if not data.get("id", None):
            data['id'] = unique_id()
        return super().to_internal_value(data)

    def create(self, validated_data):
        return super().create(validated_data)
