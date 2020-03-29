from lesson.models import Lesson, TimeTable
from lesson.serializers import (LessonModelSerializer,
                                TimeTableModelSerializer)
from utils.viewsets import BaseModelViewSet


class LessonModelViewSet(BaseModelViewSet):
    serializer_class = LessonModelSerializer
    queryset = Lesson.objects.all()


class TimeTableModelViewSet(BaseModelViewSet):
    serializer_class = TimeTableModelSerializer
    queryset = TimeTable.objects.all()
