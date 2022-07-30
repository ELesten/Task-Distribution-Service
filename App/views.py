from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import *
from rest_framework import status
from .serializer import *
from django.contrib.auth.models import User


# class Registration(APIView):
#     http_method_names = ['get', 'post']
#
#     def get(self, request):
#         return Response('OK')
#
#     def post(self, request):
#         serializer = TestSer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class DjangoUserView(ModelViewSet):
    serializer_class = DjangoUserSerializer
    queryset = User.objects.all()


class TaskView(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskCommentView(ModelViewSet):
    serializer_class = TaskCommentSerializer
    queryset = Task.objects.all()


class TaskImageView(ModelViewSet):
    serializer_class = TaskImageSerializer
    queryset = TaskImage.objects.all()


class TeamView(ModelViewSet):
    serializer_class = TeamViewSerializer
    queryset = Team.objects.all()
