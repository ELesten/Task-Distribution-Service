from django.contrib import admin
from django.urls import path, include, re_path

from .views import *
from rest_framework import routers, permissions


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
]
