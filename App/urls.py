from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from .views import *
from rest_framework import routers, permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r"comments", TaskCommentView)
router.register(r"images", TaskImageView)
router.register(r"teams", TeamView)
urlpatterns = [
    path("", include(router.urls)),
    path("drf-auth/", include("rest_framework.urls")),
    path("registration/", include("djoser.urls")),
    re_path("^auth/", include("djoser.urls.authtoken")),
    path("user-update/", UserUpdateAPIView.as_view()),
    path("task/", TaskAPIView.as_view()),
    path("all-users/", UsersList.as_view()),
    path("change-user-team/<int:pk>/", ChangeUserTeam.as_view()),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
