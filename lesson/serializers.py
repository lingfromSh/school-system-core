from utils.serializers import BaseModelSerializer, BaseHyperLinkedModelSerializer
from lesson.models import Lesson, TimeTable
from user.serializers import UserModelSerializer
from school.serializers import ClassRoomModelSerializer


class LessonModelSerializer(BaseModelSerializer):
    """Lesson 序列化"""

    class Meta:
        model = Lesson
        fields = "__all__"


class TimeTableModelSerializer(BaseModelSerializer):
    """TimeTable 序列化"""

    class Meta:
        model = TimeTable
        fields = "__all__"

    lesson = LessonModelSerializer(read_only=True)
    classroom = ClassRoomModelSerializer(read_only=True)
    teacher = UserModelSerializer(read_only=True)
    students = UserModelSerializer(many=True, read_only=True)

    def create(self, validated_data):
        super().create(validated_data)