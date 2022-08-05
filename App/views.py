from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import *
from rest_framework import status
from .serializer import *
from .models import CustomUser


class DjangoUserView(ModelViewSet):
    serializer_class = DjangoUserSerializer
    queryset = CustomUser.objects.all()


class TaskView(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskCommentView(ModelViewSet):
    serializer_class = TaskCommentSerializer
    queryset = TaskComment.objects.all()


class TaskImageView(ModelViewSet):
    serializer_class = TaskImageSerializer
    queryset = TaskImage.objects.all()


class TeamView(ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
