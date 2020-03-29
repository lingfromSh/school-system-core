from django.urls import path
from school.views import ClassRoomModelViewSet

url_patterns = [
    path("classroom/", ClassRoomModelViewSet.as_view({'get': 'list',
                                                      'post': 'create'})),
    path("classroom/<str:pk>/", ClassRoomModelViewSet.as_view({'get': 'retrieve',
                                                               'put': 'update',
                                                               'patch': 'partial_update'}))
]
