from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import status
from .permissions import *
from .serializer import *
from .models import CustomUser


class UserUpdateAPIView(APIView):
    """
    Getting and changing an authorized user.
    """

    permission_classes = [IsAuthenticated, ]
    serializer_class = DjangoUserDetailSerializer

    def get(self, request):
        serializer = self.serializer_class(
            get_object_or_404(CustomUser, id=request.user.id)
        )
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

    permission_classes = [
        IsAuthenticated,
        IsAdminOrManager,
    ]

    def get(self, request):
        result = CustomUser.objects.all()
        return Response(
            result.values("username", "team", "id"), status=status.HTTP_200_OK
        )


class ChangeUserTeam(APIView):
    """
    Add and delete members to the team
    """

    permission_classes = [
        IsAuthenticated,
        IsAdminOrManager,
    ]
    serializer_class = DjangoUsersTeamSerializer

    def get(self, request, pk):
        if request.user.role == "Manager":
            serializer = self.serializer_class(
                get_object_or_404(CustomUser.objects.filter(role="Worker"), pk=pk)
            )
        else:
            serializer = self.serializer_class(
                get_object_or_404(CustomUser.objects.all(), pk=pk)
            )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        instance = get_object_or_404(CustomUser, id=pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskModelViewSet(ModelViewSet):
    """
    CRUD for tasks with automatic filtering by role
    """
    permission_classes = [
        IsAuthenticated,
        IsAdminOrManagerOrReadOnly,
    ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = [
        "responsible_team",
        "task_status",
        "responsible_person"
    ]

    def list(self, request, *args, **kwargs):
        role = request.user.role
        if role == "Worker":
            queryset = Task.objects.filter(responsible_team=request.user.team)
        elif role == "Manager":
            team_id = request.user.managed_teams.values("id")
            queryset = Task.objects.all().filter(responsible_team__in=team_id)
        else:
            queryset = Task.objects.all()

        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeamView(ModelViewSet):
    """
    CRUD on teams for the admin without restriction
    """

    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TaskCommentView(ModelViewSet):
    """
    CRUD for comments.
    Only the admin/author has the ability to delete/modify.
    """
    permission_classes = [IsAuthenticated, ]
    serializer_class = TaskCommentSerializer
    queryset = TaskComment.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author.username != request.user.username and request.user.role != "Admin":
            return Response(status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if instance.author.username != request.user.username and request.user.role != "Admin":
            return Response(status=status.HTTP_400_BAD_REQUEST)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskImageView(ModelViewSet):
    """
    CRUD for Task image
    """
    permission_classes = [
        IsAuthenticated,
        IsAdminOrManager,
    ]
    serializer_class = TaskImageSerializer
    queryset = TaskImage.objects.all()
