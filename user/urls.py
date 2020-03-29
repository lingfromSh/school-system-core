from django.urls import path
from user.views import UserModelViewSet

url_patterns = [
    path("", UserModelViewSet.as_view({'get': 'list',
                                       'post': 'create'})),
    path("<str:pk>/", UserModelViewSet.as_view({'get': 'retrieve',
                                                'put': 'update',
                                                'patch': 'partial_update'
                                                }))
]
