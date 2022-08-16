from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsAdminOrManagerOrReadOnly, IsAdmin, IsAdminOrManager
from .serializer import *
from .models import CustomUser


class UserUpdateAPIView(APIView):
    """
    Getting and changing an authorized user.
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = DjangoUserDetailSerializer

    def get(self, request):
        serializer = self.serializer_class(get_object_or_404(CustomUser, id=request.user.id))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        instance = get_object_or_404(CustomUser, id=request.user.id)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersList(APIView):
    """
     List of all users
    """
    permission_classes = (IsAuthenticated, IsAdminOrManager)

    def get(self, request):
        result = CustomUser.objects.all()
        return Response(result.values("username", "team", "id"), status=status.HTTP_200_OK)


class ChangeUserTeam(APIView):
    """
    Add and delete members to the team
    """
    permission_classes = (IsAuthenticated, IsAdminOrManager)
    serializer_class = DjangoUsersTeamSerializer

    def get(self, request, pk):
        if request.user.role == "Manager":
            serializer = self.serializer_class(get_object_or_404(CustomUser.objects.filter(role="Worker"), pk=pk))
        else:
            serializer = self.serializer_class(get_object_or_404(CustomUser.objects.all(), pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        instance = get_object_or_404(CustomUser, id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskAPIView(APIView):
    """
    Creating and receiving tasks
    """
    permission_classes = (IsAuthenticated, IsAdminOrManagerOrReadOnly, )
    serializer_class = TaskSerializer

    def get(self, request):
        role = request.user.role
        if role == 'Worker':
            result = Task.objects.filter(responsible_team=request.user.team).values()
        elif role == 'Manager':
            team_id = request.user.managed_teams.values('id')
            result = Task.objects.all().filter(responsible_team__in=team_id).values()
        else:
            result = Task.objects.all().values()
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeamView(ModelViewSet):
    """
    Full CRUD on teams for admin
    """
    permission_classes = (IsAuthenticated, IsAdmin)
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TaskCommentView(ModelViewSet):
    serializer_class = TaskCommentSerializer
    queryset = TaskComment.objects.all()


class TaskImageView(ModelViewSet):
    serializer_class = TaskImageSerializer
    queryset = TaskImage.objects.all()


