from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'Registration', DjangoUserView) # Как связаны крад с токен авторизацией?
router.register(r'Tasks', TaskView)
router.register(r'Comments', TaskCommentView)
router.register(r'Images', TaskImageView)
router.register(r'Teams', TeamView)
urlpatterns = [
    path('', include(router.urls)),
    path('drf-auth/', include('rest_framework.urls')),
    path('registration/', include('djoser.urls')),
    path('user-update/', UsersDetailAPIView.as_view()),
    path('auth/', include('djoser.urls')),

]
