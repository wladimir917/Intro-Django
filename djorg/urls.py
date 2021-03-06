"""djorg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
# from django.urls import path, include  # include is from Day 3
from django.urls import path, include, re_path # Day 4 re_path
from rest_framework.authtoken import views

# Day 3:
from rest_framework import routers
from notes.api import PersonalNoteViewSet
from dashboard.api import StudentReportViewSet, StudentViewSet


from graphene_django.views import GraphQLView


router = routers.DefaultRouter()
router.register(r'notes', PersonalNoteViewSet)
router.register(r'dashboard', StudentReportViewSet)
router.register(r'students', StudentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # re_path(r'^api-token-auth/', views.obtain_auth_token),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    # re_path(r"^api-auth/", include("rest_framework.urls")),
    # path('rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/register/', include('rest_auth.registration.urls'))
]
