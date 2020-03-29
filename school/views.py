from school.models import ClassRoom
from school.serializers import ClassRoomModelSerializer
from rest_framework.viewsets import ModelViewSet


class ClassRoomModelViewSet(ModelViewSet):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()