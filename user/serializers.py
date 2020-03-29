from user.models import User
from utils.security import hash_password
from utils.serializers import BaseModelSerializer


class UserModelSerializer(BaseModelSerializer):
    """User 序列化"""

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        if not validated_data.get("password").startswith("argon2$"):
            validated_data['password'] = hash_password(
                validated_data['password'])
        return super().create(validated_data)
