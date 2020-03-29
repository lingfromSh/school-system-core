from django.urls import path

from lesson.views import (LessonModelViewSet,
                          TimeTableModelViewSet)

url_patterns = [
    path("time-table/", TimeTableModelViewSet.as_view({'get': 'list',
                                                       'post': 'create'})),
    path("", LessonModelViewSet.as_view({'get': 'list',
                                         'post': 'create'})),
    path("<str:pk>/", LessonModelViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'patch': 'partial_update'})),
    path("time-table/<str:pk>/", TimeTableModelViewSet.as_view({'get': 'retrieve',
                                                                'put': 'update',
                                                                'patch': 'partial_update'}))
]
