from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"comments", TaskCommentView)
router.register(r"images", TaskImageView)
router.register(r"teams", TeamView)
router.register(r"tasks", TaskModelViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("drf-auth/", include("rest_framework.urls")),
    path("registration/", include("djoser.urls")),
    path("user-update/", UserUpdateAPIView.as_view()),
    path("all-users/", UsersList.as_view()),
    path("change-user-team/<int:pk>/", ChangeUserTeam.as_view()),
]
