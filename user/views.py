from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
