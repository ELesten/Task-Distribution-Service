from django.http import HttpResponse
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from rest_framework import status
from .serializer import *
from .models import CustomUser


class TasksAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        role = request.user.role
        if role == 'Worker':
            team_id = request.user.team
            result = Task.objects.filter(responsible_team=team_id).values()
        else:
            result = Task.objects.all().values() #Для манагеров(додумать)
        return Response(result)


class UsersDetailAPIView(APIView):
    """
    Getting and changing an authorized user.
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = DjangoUserDetailSerializer

    def get(self, request):
        serializer = self.serializer_class(get_object_or_404(CustomUser, id=request.user.id))
        return Response(serializer.data)

    def patch(self, request):
        instance = get_object_or_404(CustomUser, id=request.user.id)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TeamView(ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

# class DjangoUserView(ModelViewSet):
#     serializer_class = DjangoUserSerializer
#     queryset = CustomUser.objects.all()


class TaskView(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskCommentView(ModelViewSet):
    serializer_class = TaskCommentSerializer
    queryset = TaskComment.objects.all()


class TaskImageView(ModelViewSet):
    serializer_class = TaskImageSerializer
    queryset = TaskImage.objects.all()


