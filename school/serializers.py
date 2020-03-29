from utils.serializers import BaseModelSerializer
from school.models import ClassRoom


class ClassRoomModelSerializer(BaseModelSerializer):
    """教室序列化"""

    class Meta:
        model = ClassRoom
        fields = "__all__"
