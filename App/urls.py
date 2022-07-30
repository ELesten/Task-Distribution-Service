from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Users', CustomUserView)
router.register(r'Tasks', TaskView)
router.register(r'Comments', TaskCommentView)
router.register(r'Images', TaskImageView)
router.register(r'Teams', TeamView)
urlpatterns = [
    # path('register/', Registration.as_view()),
    path('', include(router.urls)),

]
