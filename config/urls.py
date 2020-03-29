"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from user.urls import url_patterns as user_urls
from lesson.urls import url_patterns as lessons_url
from school.urls import url_patterns as school_urls

urlpatterns = [
    path("api-doc/", include_docs_urls(title="School-System-API-Doc")),
    path("user/", include(user_urls)),
    path("lesson/", include(lessons_url)),
    path("school/", include(school_urls)),
]
